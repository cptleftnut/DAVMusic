#!/usr/bin/env python3
"""
DAVMusic - Brugbar inference script (tilpasset til Nicklas / cptleftnut / DAVLm)
==================================================================================

Dette script gør det nemt at generere musik med modellen:
https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot

Brug:
    python generate.py --help

Eksempler på prompts (kopier og brug):
--------------------------------------
# 1. Energetic Pop (engelsk)
--lyrics "[verse]\nI walk alone through the neon lights\nSearching for something that feels right\n\n[chorus]\nThis is my night, this is my fight\nDancing in the dark until the morning light" \
--genre "energetic male vocal pop electronic upbeat bright vocal"

# 2. Melankolsk Indie (dansk/engelsk mix)
--lyrics "[verse]\nRegnen falder stille på de tomme gader\nJeg tænker på dig igen i nat\n\n[chorus]\nKom hjem til mig, min kære\nJeg savner dig så meget" \
--genre "melancholic male vocal indie folk acoustic emotional soft vocal"

# 3. Upbeat Dance / EDM
--lyrics "[verse]\nLights are flashing, bodies moving on the floor\nFeel the bass inside your core\n\n[drop]\nWe dance until the morning comes\nThis is where we belong" \
--genre "energetic female vocal edm dance upbeat electronic festival vocal bright"

# 4. Lo-fi Chill
--lyrics "[verse]\nRain tapping on the window pane\nCoffee in my hand, no rush today\n\n[chorus]\nJust breathing slow, letting go\nIn this quiet moment" \
--genre "chill male vocal lofi hiphop relaxed jazzy soft vocal warm"

Output gemmes i ../output/

Krav:
- God GPU (mindst 24GB VRAM anbefales til fuld sang)
- Miljø sat op som i README.md
- HF token sat (huggingface-cli login) hvis nødvendigt for download

"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="DAVMusic - Nem musikgenerering med YuE-modellen (tilpasset til Nicklas / cptleftnut / DAVLm)"
    )
    parser.add_argument(
        "--lyrics",
        type=str,
        default="[verse]\nI walk alone through the neon lights\nSearching for something that feels right\n\n[chorus]\nThis is my night, this is my fight\nDancing in the dark until the morning light",
        help="Sangtekster med [verse], [chorus] osv. Brug \\n\\n mellem sektioner."
    )
    parser.add_argument(
        "--genre",
        type=str,
        default="energetic male vocal pop electronic upbeat bright vocal",
        help="Genre tags (5 komponenter anbefales: genre, instrument, mood, gender, timbre)"
    )
    parser.add_argument(
        "--segments",
        type=int,
        default=2,
        help="Antal segmenter (vers + omkvæd osv.). 2 er godt til test."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="../output",
        help="Mappe hvor lydfiler gemmes"
    )
    parser.add_argument(
        "--stage1_model",
        type=str,
        default="m-a-p/YuE-s1-7B-anneal-en-cot",
        help="Stage 1 model (den du bad om)"
    )
    parser.add_argument(
        "--stage2_model",
        type=str,
        default="m-a-p/YuE-s2-1B-general",
        help="Stage 2 model"
    )
    parser.add_argument(
        "--cuda_idx",
        type=int,
        default=0,
        help="GPU index (0 for første GPU)"
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=3000,
        help="Maks tokens pr. segment (~30 sekunder lyd)"
    )

    args = parser.parse_args()

    # Sørg for at output mappen findes
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("DAVMusic Inference - Nicklas / cptleftnut / DAVLm")
    print(f"Bruger model: {args.stage1_model}")
    print("=" * 60)

    # Byg kommandoen til den originale infer.py
    # Antager at scriptet køres fra inference/ mappen
    cmd = [
        sys.executable, "infer.py",
        "--cuda_idx", str(args.cuda_idx),
        "--stage1_model", args.stage1_model,
        "--stage2_model", args.stage2_model,
        "--genre_txt", "genre_temp.txt",
        "--lyrics_txt", "lyrics_temp.txt",
        "--run_n_segments", str(args.segments),
        "--stage2_batch_size", "4",
        "--output_dir", str(output_path),
        "--max_new_tokens", str(args.max_new_tokens),
        "--repetition_penalty", "1.1"
    ]

    # Opret midlertidige prompt filer
    with open("genre_temp.txt", "w", encoding="utf-8") as f:
        f.write(args.genre)

    with open("lyrics_temp.txt", "w", encoding="utf-8") as f:
        f.write(args.lyrics.replace("\\n", "\n"))

    print("\nKører inference...")
    print("Dette kan tage 2-6 minutter afhængig af GPU og længde.\n")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Fejl under inference:")
        print(e.stdout)
        print(e.stderr)
        print("\nTip: Sørg for at du er i inference/ mappen og har kørt setup fra README.md")
        sys.exit(1)
    finally:
        # Ryd op i midlertidige filer
        for temp_file in ["genre_temp.txt", "lyrics_temp.txt"]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    print("\n✅ Færdig! Tjek mappen:", output_path)
    print("Der skulle nu være genererede .wav eller .mp3 filer.")

if __name__ == "__main__":
    main()
