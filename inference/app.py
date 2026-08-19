#!/usr/bin/env python3
"""
DAVMusic Gradio Web UI
======================

En brugervenlig web-grænseflade til DAVMusic / YuE-modellen.
Opdateret med support for ICL (In-Context Learning) / Stemmekloning.

Kør:
    python app.py
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
    }
]

def get_example(index):
    ex = EXAMPLES[index]
    return ex["lyrics"], ex["genre"]

def run_inference(lyrics, genre, segments, mode, model_name, audio_prompt, progress=gr.Progress()):
    """
    Wrapper der kalder infer.py med de valgte parametre.
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
        "--stage1_model", model_name,
        "--stage2_model", "m-a-p/YuE-s2-1B-general",
        "--genre_txt", genre_file,
        "--lyrics_txt", lyrics_file,
        "--run_n_segments", str(segments),
        "--stage2_batch_size", "2",
        "--output_dir", str(output_dir),
        "--max_new_tokens", "3000",
        "--repetition_penalty", "1.1"
    ]

    if mode == "ICL (med audio prompt)":
        if audio_prompt is None:
            return None, "❌ Fejl: Du skal uploade en reference-lydfil for at bruge ICL mode."
        
        cmd.append("--use_audio_prompt")
        cmd.extend(["--audio_prompt_path", audio_prompt])
        
        # Tip: YuE kræver ofte at man angiver om det er vokal eller mix
        # Her antager vi dual-track eller single-track baseret på infer.py standard
        # Man kan tilføje flere parametre her hvis nødvendigt

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=900  # 15 minutter
        )

        progress(0.9, desc="Færdigbehandler...")

        # Find genereret fil
        generated_files = list(output_dir.glob("*.wav")) + list(output_dir.glob("*.mp3"))
        if generated_files:
            latest = max(generated_files, key=os.path.getctime)
            return str(latest), f"✅ Generering færdig!\n\n{result.stdout[-500:]}"
        else:
            return None, f"❌ Ingen lydfil fundet.\n\nOutput:\n{result.stdout}\n\nFejl:\n{result.stderr}"

    except subprocess.TimeoutExpired:
        return None, "⏱️ Timeout – genereringen tog for lang tid."
    except Exception as e:
        return None, f"❌ Fejl: {str(e)}"
    finally:
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
        css=".gradio-container { max-width: 950px !important; margin: auto; }"
    ) as demo:

        gr.Markdown("""
        # 🎵 DAVMusic – AI Musik Generator
        **Tilpasset til Nicklas / cptleftnut / DAVLm**  
        Nu med support for stemmekloning (ICL).
        """)

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 1. Model & Indstillinger")
                model_input = gr.Dropdown(
                    choices=[
                        "m-a-p/YuE-s1-7B-anneal-en-cot", 
                        "m-a-p/YuE-s1-7B-anneal-en-icl",
                        "DAVLm/DAVMusic-s1-7B-anneal-en-cot",
                        "DAVLm/DAVMusic-s1-7B-anneal-en-icl"
                    ],
                    value="m-a-p/YuE-s1-7B-anneal-en-cot",
                    label="Vælg Model (Brug 'icl' til stemmekloning)"
                )
                
                mode_radio = gr.Radio(
                    ["CoT (tekst kun)", "ICL (med audio prompt)"],
                    value="CoT (tekst kun)",
                    label="Generation Mode"
                )

                audio_prompt_input = gr.Audio(
                    label="Reference Lyd (kun til ICL)",
                    type="filepath",
                    visible=False
                )
                
                # Vis/skjul lydfelt baseret på mode
                def update_visibility(mode):
                    return gr.update(visible=(mode == "ICL (med audio prompt)"))
                
                mode_radio.change(fn=update_visibility, inputs=mode_radio, outputs=audio_prompt_input)

                segments_slider = gr.Slider(
                    minimum=1, maximum=4, value=2, step=1,
                    label="Antal segmenter"
                )

            with gr.Column(scale=1):
                gr.Markdown("### 2. Tekst & Genre")
                lyrics_input = gr.Textbox(
                    label="Lyrics ([verse], [chorus] osv.)",
                    placeholder="Indtast sangtekster...",
                    lines=6,
                    value=EXAMPLES[0]["lyrics"]
                )

                genre_input = gr.Textbox(
                    label="Genre tags",
                    placeholder="energetic male vocal pop...",
                    value=EXAMPLES[0]["genre"]
                )

                generate_btn = gr.Button("🚀 Generér Musik", variant="primary", size="lg")

        with gr.Row():
            with gr.Column():
                gr.Markdown("### 3. Resultat")
                audio_output = gr.Audio(label="Genereret Lyd", type="filepath")
                status_output = gr.Textbox(label="Status Log", lines=4, interactive=False)

        # Eksempler
        gr.Markdown("### ✨ Hurtige eksempler")
        with gr.Row():
            for i, ex in enumerate(EXAMPLES):
                btn = gr.Button(ex["title"], size="sm")
                btn.click(
                    fn=lambda idx=i: get_example(idx),
                    inputs=[],
                    outputs=[lyrics_input, genre_input]
                )

        generate_btn.click(
            fn=run_inference,
            inputs=[lyrics_input, genre_input, segments_slider, mode_radio, model_input, audio_prompt_input],
            outputs=[audio_output, status_output],
            show_progress=True
        )

    return demo

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )
