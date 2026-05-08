#!/usr/bin/env python3
"""
DAVMusic Gradio Web UI
======================

En brugervenlig web-grænseflade til DAVMusic / YuE-modellen.

Kør:
    python app.py

Så åbner den automatisk i browseren (eller brug --share til offentlig link).

Funktioner:
- Tekstfelt til sangtekster med [verse], [chorus] support
- Genre tags input
- Antal segmenter slider
- Mode valg (CoT / ICL)
- Direkte afspilning af genereret lyd
- Flere eksempler klar til brug

Forudsætninger:
- inference/ mappen med infer.py, tokenizer og xcodec skal være til stede
- God GPU anbefales (24GB+ VRAM)
"""

import gradio as gr
import os
import subprocess
import tempfile
from pathlib import Path
import shutil

# ============================================================
# Hjælpefunktioner
# ============================================================

EXAMPLES = [
    {
        "title": "Energetic Pop",
        "lyrics": "[verse]\nI walk alone through the neon lights\nSearching for something that feels right\n\n[chorus]\nThis is my night, this is my fight\nDancing in the dark until the morning light",
        "genre": "energetic male vocal pop electronic upbeat bright vocal"
    },
    {
        "title": "Melankolsk Indie (dansk)",
        "lyrics": "[verse]\nRegnen falder stille på de tomme gader\nJeg tænker på dig igen i nat\n\n[chorus]\nKom hjem til mig, min kære\nJeg savner dig så meget",
        "genre": "melancholic male vocal indie folk acoustic emotional soft vocal"
    },
    {
        "title": "Upbeat Dance / EDM",
        "lyrics": "[verse]\nLights are flashing, bodies moving on the floor\nFeel the bass inside your core\n\n[drop]\nWe dance until the morning comes\nThis is where we belong",
        "genre": "energetic female vocal edm dance upbeat electronic festival vocal bright"
    },
    {
        "title": "Lo-fi Chill",
        "lyrics": "[verse]\nRain tapping on the window pane\nCoffee in my hand, no rush today\n\n[chorus]\nJust breathing slow, letting go\nIn this quiet moment",
        "genre": "chill male vocal lofi hiphop relaxed jazzy soft vocal warm"
    }
]

def get_example(index):
    ex = EXAMPLES[index]
    return ex["lyrics"], ex["genre"], ex["title"]

def run_inference(lyrics, genre, segments, mode, progress=gr.Progress()):
    """
    Wrapper der kalder infer.py med de valgte parametre.
    Returnerer sti til genereret lydfil (eller fejlbesked).
    """
    progress(0, desc="Forbereder...")

    output_dir = Path("../output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Opret midlertidige prompt-filer
    genre_file = "genre_ui_temp.txt"
    lyrics_file = "lyrics_ui_temp.txt"

    with open(genre_file, "w", encoding="utf-8") as f:
        f.write(genre.strip())

    with open(lyrics_file, "w", encoding="utf-8") as f:
        f.write(lyrics.strip())

    progress(0.2, desc="Kører inference... (kan tage flere minutter)")

    cmd = [
        "python", "infer.py",
        "--cuda_idx", "0",
        "--stage1_model", "m-a-p/YuE-s1-7B-anneal-en-cot",
        "--stage2_model", "m-a-p/YuE-s2-1B-general",
        "--genre_txt", genre_file,
        "--lyrics_txt", lyrics_file,
        "--run_n_segments", str(segments),
        "--stage2_batch_size", "2",   # Lavere for at spare hukommelse
        "--output_dir", str(output_dir),
        "--max_new_tokens", "3000",
        "--repetition_penalty", "1.1"
    ]

    if mode == "ICL (med audio prompt)":
        # ICL mode kan udvides senere med audio upload
        cmd.append("--use_audio_prompt")  # Simpel version

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10 minutter timeout
        )

        progress(0.9, desc="Færdigbehandler...")

        # Find genereret fil (infer.py laver normalt .wav eller .mp3)
        generated_files = list(output_dir.glob("*.wav")) + list(output_dir.glob("*.mp3"))
        if generated_files:
            latest = max(generated_files, key=os.path.getctime)
            return str(latest), f"✅ Generering færdig!\n\n{result.stdout[-500:]}"
        else:
            return None, f"❌ Ingen lydfil fundet.\n\nOutput:\n{result.stdout}\n\nFejl:\n{result.stderr}"

    except subprocess.TimeoutExpired:
        return None, "⏱️ Timeout – genereringen tog for lang tid. Prøv færre segmenter eller kortere tekst."
    except Exception as e:
        return None, f"❌ Fejl: {str(e)}"
    finally:
        # Ryd op
        for f in [genre_file, lyrics_file]:
            if os.path.exists(f):
                os.remove(f)

# ============================================================
# Gradio Interface
# ============================================================

def create_ui():
    with gr.Blocks(
        title="DAVMusic – AI Musik Generator",
        theme=gr.themes.Soft(primary_hue="blue"),
        css="""
        .gradio-container { max-width: 900px !important; margin: auto; }
        .example-btn { margin: 4px; }
        """
    ) as demo:

        gr.Markdown("""
        # 🎵 DAVMusic – AI Musik Generator
        **Bruger modellen:** m-a-p/YuE-s1-7B-anneal-en-cot  
        Tilpasset til Nicklas / cptleftnut / DAVLm
        """)

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📝 Sangtekster")
                lyrics_input = gr.Textbox(
                    label="Lyrics (brug [verse], [chorus], [bridge] osv.)",
                    placeholder="Indtast sangtekster her...",
                    lines=8,
                    value=EXAMPLES[0]["lyrics"]
                )

                gr.Markdown("### 🎨 Genre Tags")
                genre_input = gr.Textbox(
                    label="Genre tags (5 komponenter anbefales)",
                    placeholder="energetic male vocal pop electronic upbeat",
                    value=EXAMPLES[0]["genre"]
                )

                segments_slider = gr.Slider(
                    minimum=1, maximum=4, value=2, step=1,
                    label="Antal segmenter (1 = kort test, 2-3 = normal sang)"
                )

                mode_radio = gr.Radio(
                    ["CoT (tekst kun)", "ICL (med audio prompt)"],
                    value="CoT (tekst kun)",
                    label="Generation Mode"
                )

                generate_btn = gr.Button("🚀 Generér Musik", variant="primary", size="lg")

            with gr.Column(scale=1):
                gr.Markdown("### 🎧 Genereret Lyd")
                audio_output = gr.Audio(label="Resultat", type="filepath")
                status_output = gr.Textbox(label="Status / Log", lines=6, interactive=False)

        # Eksempler
        gr.Markdown("### ✨ Hurtige eksempler (klik for at indlæse)")
        with gr.Row():
            for i, ex in enumerate(EXAMPLES):
                btn = gr.Button(ex["title"], size="sm")
                btn.click(
                    fn=lambda idx=i: get_example(idx),
                    inputs=[],
                    outputs=[lyrics_input, genre_input]
                )

        # Kør inference når knappen trykkes
        generate_btn.click(
            fn=run_inference,
            inputs=[lyrics_input, genre_input, segments_slider, mode_radio],
            outputs=[audio_output, status_output],
            show_progress=True
        )

        gr.Markdown("""
        ---
        **Tip:** Start altid med 1 segment og kort tekst for at teste.  
        Fulde sange kræver meget GPU-hukommelse (24GB+ anbefales).  
        Har du problemer? Tjek README eller kør `python generate.py --help`.
        """)

    return demo

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,           # Giver offentligt link (nyttigt i Colab)
        inbrowser=True
    )
