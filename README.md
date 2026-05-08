<p align="center">
    <picture>
        <source srcset="./assets/logo/黑底.svg" media="(prefers-color-scheme: dark)">
        <img src="./assets/logo/白底.svg" width="40%">
    </picture>
</p>

<p align="center">
    <a href="https://cptleftnut.github.io/DAVMusic/">Demo 🎶</a> &nbsp;|&nbsp; 📑 <a href="https://arxiv.org/abs/2503.08638">Paper (baseret på original YuE)</a>
    <br>
    <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-en-cot">DAVMusic-s1-7B-anneal-en-cot 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-en-icl">DAVMusic-s1-7B-anneal-en-icl 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-jp-kr-cot">DAVMusic-s1-7B-anneal-jp-kr-cot 🤗</a>
    <br>
    <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-jp-kr-icl">DAVMusic-s1-7B-anneal-jp-kr-icl 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-zh-cot">DAVMusic-s1-7B-anneal-zh-cot 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/DAVLm/DAVMusic-s1-7B-anneal-zh-icl">DAVMusic-s1-7B-anneal-zh-icl 🤗</a>
    <br>
    <a href="https://huggingface.co/DAVLm/DAVMusic-s2-1B-general">DAVMusic-s2-1B-general 🤗</a> &nbsp;|&nbsp; <a href="https://huggingface.co/DAVLm/DAVMusic-upsampler">DAVMusic-upsampler 🤗</a>
</p>

---

**Bemærk om tilpasning:** Denne README er en tilpasset version af den originale [YuE repository](https://github.com/multimodal-art-projection/YuE) til dit repository "DAVMusic" (https://github.com/cptleftnut/DAVMusic) under organisationen DAVLm. Den underliggende teknologi og kode er baseret på det originale arbejde af multimodal-art-projection. Husk at kreditere det originale arbejde og citere papiret passende for at overholde open source-licensen (Apache 2.0) og god akademisk praksis.

---

Vores models navn er **DAVMusic**. Nogle af jer kan have svært ved at udtale visse navne. Hvis det er tilfældet, kan I bare kalde det "DAVMusic". Vi har skrevet en sang med vores models navn, se [her](assets/logo/davmusic.mp3) (tilpas filen efter behov).

DAVMusic er en banebrydende serie af open-source foundation models designet til musikgenerering, specifikt til at transformere sangtekster til fulde sange (lyrics2song). Den kan generere en komplet sang, der varer flere minutter, inklusive både en catchy vokalspor og akkompagnementspor. DAVMusic er i stand til at modellere forskellige genrer/sprog/vokale teknikker. Besøg venligst [**Demo-siden**](https://cptleftnut.github.io/DAVMusic/) for fantastisk vokalpræstation.

## Nyheder og opdateringer
* 📌 Join os på Discord! [<img alt="join discord" src="https://img.shields.io/discord/842440537755353128?color=%237289da&logo=discord"/>](https://discord.gg/ssAyWMnMzu) (tilpas link)

* **2025.06.04 🔥** Nu understøtter DAVMusic LoRA finetune.
* **2025.03.12 🔥 Paper udgivet🎉**: Vi udgiver nu [DAVMusic teknisk rapport](https://arxiv.org/abs/2503.08638) (baseret på original YuE)!!! Vi diskuterer alle de tekniske detaljer, resultater og erfaringer. Nyd det, og citér os gerne~
* **2025.03.11 🫶** Nu understøtter DAVMusic inkrementel sanggenerering!!! Se [DAVMusic-UI](https://github.com/cptleftnut/DAVMusic-UI) (opret gerne din egen Gradio UI).
* **2025.02.17 🫶** Nu understøtter DAVMusic musikfortsættelse og Google Colab! Se [DAVMusic-extend](https://github.com/cptleftnut/DAVMusic-extend).
* **2025.02.07 🎉** Få DAVMusic til Windows på [pinokio](https://pinokio.computer).

* **2025.01.30 🔥 Inference Update**: Vi understøtter nu dual-track ICL mode! Du kan promte modellen med en referencesang, og den vil generere en ny sang i lignende stil (voice cloning, music style transfer osv.). Prøv det! 🔥🔥🔥

* **2025.01.30 🔥 Meddelelse: En ny æra under Apache 2.0 🔥**: Vi er glade for at annoncere, at **DAVMusic** nu officielt er licenseret under **Apache 2.0** licensen. Vi håber oprigtigt, at dette markerer et vendepunkt for musikgenerering og kreativ AI.

* **2025.01.29 🎉**: Vi har opdateret licensbeskrivelsen. Vi **OPFORDRER** kunstnere og indholdsskabere til at sample og inkorporere outputs genereret af vores model i deres egne værker og endda tjene penge på dem. Det eneste krav er at kreditere vores navn: **DAVMusic by Nicklas** (alfabetisk rækkefølge).
* **2025.01.28 🫶**: Tak til Nicklas og fællesskabet for tutorials og bidrag.
* **2025.01.26 🔥**: Vi har udgivet **DAVMusic** serien.

* **2026.05.08 🚀 Nyttige Hugging Face Ressourcer**:
    * [Reachy Mini Spaces](https://huggingface.co/spaces?filter=reachy_mini)
    * [Reachy Mini Simulation Guide](https://huggingface.co/docs/reachy_mini/platforms/simulation/get_started)

<br>

---
## TODOs📋

- [ ] Support stemgen mode https://github.com/cptleftnut/DAVMusic/issues/21
- [ ] Support llama.cpp https://github.com/ggerganov/llama.cpp/issues/11467
- [ ] Support transformers tensor parallel. https://github.com/cptleftnut/DAVMusic/issues/7
- [ ] Online serving on huggingface space.
- [ ] Support vLLM and sglang https://github.com/cptleftnut/DAVMusic/issues/66
- [x] Release paper to Arxiv.
- [x] Example LoRA finetune code using 🤗 Transformers.
- [x] Support Colab: [DAVMusic-extend](https://github.com/cptleftnut/DAVMusic-extend)
- [x] Support gradio interface. https://github.com/cptleftnut/DAVMusic/issues/1
- [x] Support dual-track ICL mode.
- [x] Fix "instrumental" naming bug in output files. https://github.com/cptleftnut/DAVMusic/pull/26
- [x] Support seeding https://github.com/cptleftnut/DAVMusic/issues/20
- [x] Allow `--repetition_penalty` to customize repetition penalty. https://github.com/cptleftnut/DAVMusic/issues/45

---

## Hardware og ydeevne

### **GPU-hukommelse**
DAVMusic kræver betydelig GPU-hukommelse til generering af lange sekvenser. Nedenfor er de anbefalede konfigurationer:
- **For GPU'er med 24GB hukommelse eller mindre**: Kør **op til 2 sessioner** for at undgå out-of-memory (OOM) fejl. Takket være fællesskabet findes der alternativer som [DAVMusic-exllamav2](https://github.com/cptleftnut/DAVMusic-exllamav2) og [DAVMusicGP](https://github.com/cptleftnut/DAVMusicGP) til dem med begrænsede GPU-ressourcer.
- **Til fuld sanggenerering** (mange sessioner, f.eks. 4 eller flere): Brug **GPU'er med mindst 80GB hukommelse**. f.eks. H800, A100 eller flere RTX4090s med tensor parallel.

For at tilpasse antallet af sessioner tillader interfacet dig at specificere det ønskede sessionsantal. Som standard kører modellen **2 sessioner** (1 vers + 1 omkvæd) for at undgå OOM-problemer.

### **Eksekveringstid**
På en **H800 GPU** tager generering af 30s lyd **150 sekunder**.
På en **RTX 4090 GPU** tager generering af 30s lyd cirka **360 sekunder**. 

---

## 🪟 Windows-brugere Quickstart
- Til en **one-click installer**, brug [Pinokio](https://pinokio.computer).  
- Til **Gradio med Docker**, se: [DAVMusic-for-Windows](https://github.com/cptleftnut/DAVMusic-for-windows)

## ⚡ Nem generering med generate.py (anbefalet til dig)

Vi har lavet et brugervenligt script specielt til dig, der bruger **præcis den model** du bad om:

**https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot**

Scriptet ligger i `inference/generate.py` og lader dig angive sangtekster og genre direkte på kommandolinjen.

### Trin-for-trin (Linux / WSL / macOS)

1. Sørg for at du har hele `inference/` mappen fra det originale YuE-repo (eller kopiér den ind i dit DAVMusic repo).

2. Gå ind i mappen:
   ```bash
   cd DAVMusic/inference
   ```

3. Kør det brugbare script (eksempel):
   ```bash
   python generate.py \
       --lyrics "[verse]\nI walk alone through the neon lights\nSearching for something that feels right\n\n[chorus]\nThis is my night, this is my fight\nDancing in the dark until the morning light" \
       --genre "energetic male vocal pop electronic upbeat bright vocal" \
       --segments 2
   ```

4. Outputtet lander i `../output/` mappen.

Du kan også ændre model med `--stage1_model` hvis du senere uploader din egen version til `DAVLm`.

**Tip:** Sæt din Hugging Face token først med:
```bash
huggingface-cli login
```
(Brug det token du har – gem det aldrig i offentlige filer!)

## 🖥️ Fuld Gradio Web-UI

For den bedste oplevelse har vi lavet en moderne web-grænseflade:

**Fil:** `inference/app.py`

**Funktioner:**
- Tekstfelt til sangtekster med support for `[verse]`, `[chorus]` osv.
- Genre tags input
- Slider til antal segmenter
- Mode-valg (CoT / ICL)
- Direkte afspilning af genereret lyd i browseren
- 4 færdige eksempler (klik og generér)

### Kør lokalt:
```bash
cd inference
python app.py
```

Appen åbner automatisk i browseren på `http://localhost:7860`.

## ☁️ Google Colab (gratis GPU – stærkt anbefalet)

Den nemmeste måde at komme i gang på er via Google Colab:
	
	**Fil:** `notebooks/DAVMusic_Colab_Notebook.ipynb`
	
	1. Åbn eller upload notebooken til [Google Colab](https://colab.research.google.com)
	2. Kør alle celler (Runtime → Run all)
	3. Når Gradio starter, klik på det offentlige link
	
	Colab giver dig gratis T4 GPU, hvilket er meget bedre end en telefon eller lokal CPU. Den nye struktur i repositoryet er optimeret til Colab.

## 🐧 Linux/WSL-brugere Quickstart
Til en **hurtig start**, se video tutorials fra fællesskabet eller opret din egen.  
Hvis du er ny til **machine learning** eller **kommandolinjen**, anbefaler vi stærkt at se videoen først.  

Til at bruge en **GUI/Gradio** grænseflade, tjek:
- [DAVMusic-exllamav2-UI](https://github.com/cptleftnut/DAVMusic-exllamav2-UI)
- [DAVMusicGP](https://github.com/cptleftnut/DAVMusicGP)
- [DAVMusic-Interface](https://github.com/cptleftnut/DAVMusic-Interface)  

### 1. Installer miljø og afhængigheder
Sørg for at installere flash attention 2 korrekt for at reducere VRAM-forbrug. 
```bash
# Vi anbefaler at bruge conda til at oprette et nyt miljø.
conda create -n davmusic python=3.8 # Python >=3.8 anbefales.
conda activate davmusic
# installer cuda >= 11.8
conda install pytorch torchvision torchaudio cudatoolkit=11.8 -c pytorch -c nvidia
pip install -r <(curl -sSL https://raw.githubusercontent.com/cptleftnut/DAVMusic/main/requirements.txt)

# For at spare GPU-hukommelse er FlashAttention 2 obligatorisk. 
# Uden det kan lang lyd føre til out-of-memory (OOM) fejl.
# Vær opmærksom på at matche cuda-versionen og flash-attn-versionen
pip install flash-attn --no-build-isolation
```
### 2. Download infer-koden og tokenizer
```bash
# Sørg for at have git-lfs installeret (https://git-lfs.com)
# hvis du ikke har root, se https://github.com/git-lfs/git-lfs/issues/4134#issuecomment-1635204943
sudo apt update
sudo apt install git-lfs
git lfs install
git clone https://github.com/cptleftnut/DAVMusic.git

cd DAVMusic/inference/
git clone https://huggingface.co/DAVLm/xcodec_mini_infer
```
### 3. Kør inferensen
Generer nu musik med **DAVMusic** ved hjælp af 🤗 Transformers. Sørg for at trin [1](#1-installer-miljø-og-afhængigheder) og [2](#2-download-infer-koden-og-tokenizer) er korrekt opsat. 

Bemærk:
- Sæt `--run_n_segments` til antallet af sangtekstsektioner, hvis du vil generere en fuld sang. Du kan også øge `--stage2_batch_size` baseret på din tilgængelige GPU-hukommelse.
- Du kan tilpasse prompten i `genre.txt` og `lyrics.txt`. Se prompt engineering guide [her](#prompt-engineering-guide).
- Du kan øge `--stage2_batch_size` for at fremskynde inferensen, but vær forsigtig med OOM.
- LM ckpts vil automatisk blive downloadet fra huggingface. 

```bash
# Dette er CoT mode.
cd DAVMusic/inference/
python infer.py \
    --cuda_idx 0 \
    --stage1_model DAVLm/DAVMusic-s1-7B-anneal-en-cot \
    --stage2_model DAVLm/DAVMusic-s2-1B-general \
    --genre_txt ../prompt_egs/genre.txt \
    --lyrics_txt ../prompt_egs/lyrics.txt \
    --run_n_segments 2 \
    --stage2_batch_size 4 \
    --output_dir ../output \
    --max_new_tokens 3000 \
    --repetition_penalty 1.1
```

Vi understøtter også musik in-context-learning (giv en referencesang), der er 2 typer: single-track (mix/vocal/instrumental) og dual-track. 

Bemærk: 
- ICL kræver en anden ckpt, f.eks. `DAVLm/DAVMusic-s1-7B-anneal-en-icl`.
- Musik ICL kræver generelt et 30s lydsegment. Modellen vil skrive nye sange med lignende stil som den angivne lyd og kan forbedre musicality.
- Dual-track ICL fungerer generelt bedre og kræver både vokal- og instrumentalspor.
- Til single-track ICL kan du give et mix, vokal- eller instrumentalspor.
- Du kan adskille vokal- og instrumentalspor ved hjælp af [python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) eller [Ultimate Vocal Remover GUI](https://github.com/Anjok07/ultimatevocalremovergui).

```bash
# Dette er dual-track ICL mode.
# For at slå dual-track mode til, aktiver `--use_dual_tracks_prompt`
# og angiv `--vocal_track_prompt_path`, `--instrumental_track_prompt_path`, 
# `--prompt_start_time` og `--prompt_end_time`
# Ref-lyden er taget fra GTZAN test set.
cd DAVMusic/inference/
python infer.py \
    --cuda_idx 0 \
    --stage1_model DAVLm/DAVMusic-s1-7B-anneal-en-icl \
    --stage2_model DAVLm/DAVMusic-s2-1B-general \
    --genre_txt ../prompt_egs/genre.txt \
    --lyrics_txt ../prompt_egs/lyrics.txt \
    --run_n_segments 2 \
    --stage2_batch_size 4 \
    --output_dir ../output \
    --max_new_tokens 3000 \
    --repetition_penalty 1.1 \
    --use_dual_tracks_prompt \
    --vocal_track_prompt_path ../prompt_egs/pop.00001.Vocals.mp3 \
    --instrumental_track_prompt_path ../prompt_egs/pop.00001.Instrumental.mp3 \
    --prompt_start_time 0 \
    --prompt_end_time 30 
```

```bash
# Dette er single-track (mix/vocal/instrumental) ICL mode.
# For at slå single-track ICL til, aktiver `--use_audio_prompt`, 
# og angiv `--audio_prompt_path` , `--prompt_start_time` og `--prompt_end_time`. 
# Ref-lyden er taget fra GTZAN test set.
cd DAVMusic/inference/
python infer.py \
    --cuda_idx 0 \
    --stage1_model DAVLm/DAVMusic-s1-7B-anneal-en-icl \
    --stage2_model DAVLm/DAVMusic-s2-1B-general \
    --genre_txt ../prompt_egs/genre.txt \
    --lyrics_txt ../prompt_egs/lyrics.txt \
    --run_n_segments 2 \
    --stage2_batch_size 4 \
    --output_dir ../output \
    --max_new_tokens 3000 \
    --repetition_penalty 1.1 \
    --use_audio_prompt \
    --audio_prompt_path ../prompt_egs/pop.00001.mp3 \
    --prompt_start_time 0 \
    --prompt_end_time 30 
```
---

## Prompt Engineering Guide
Prompten består af tre dele: genre tags, sangtekster og ref audio.

### Genre Tagging Prompt
1. Et eksempel på genre tagging prompt kan findes [her](prompt_egs/genre.txt).
2. En stabil tagging prompt består normalt af fem komponenter: genre, instrument, mood, gender og timbre. Alle fem bør inkluderes hvis muligt, adskilt af mellemrum (space delimiter).
3. Selvom vores tags har et åbent ordforråd, har vi leveret de 200 mest almindeligt anvendte [tags](./top_200_tags.json). Det anbefales at vælge tags fra denne liste for mere stabile resultater.
4. Rækkefølgen af tags er fleksibel. For eksempel kan en stabil genre tagging prompt se sådan ud: "inspiring female uplifting pop airy vocal electronic bright vocal vocal."
5. Derudover har vi introduceret "Mandarin" og "Cantonese" tags for at skelne mellem dem.

### Lyrics Prompt
1. Et eksempel på lyric prompt kan findes [her](prompt_egs/lyrics.txt).
2. Vi understøtter flere sprog, inklusive men ikke begrænset til engelsk, mandarin kinesisk, kantonesisk, japansk og koreansk.
3. Lyrics prompten bør opdeles i sessioner med struktur labels (f.eks. [verse], [chorus], [bridge], [outro]) foranstillet. Hver session skal adskilles af 2 newline tegn "\n\n".
4. **UNDGÅ** at putte for mange ord i en enkelt segment, da hver session er omkring 30s (`--max_new_tokens 3000` som standard).
5. Vi finder at [intro] label er mindre stabil, så vi anbefaler at starte med [verse] eller [chorus].
6. Til generering af musik uden vokal (kun instrumental), se relevant issue i det originale repo.

### Audio Prompt
1. Audio prompt er valgfri. At give ref audio til ICL øger normalt den gode case rate og resulterer i mindre diversitet, da det genererede token space er bundet af ref audio. CoT only (ingen ref) vil resultere i mere divers output.
2. Vi finder at dual-track ICL mode giver den bedste musicality og prompt following. 
3. Brug omkvædsdelen af musikken som prompt for bedre musicality.
4. Omkring 30s audio anbefales til ICL.
5. Til musikfortsættelse, se [DAVMusic-extend](https://github.com/cptleftnut/DAVMusic-extend).

---

## License Agreement & Disclaimer  
- DAVMusic modellen (inklusive dens vægte) er nu udgivet under **Apache License, Version 2.0**. Vi tjener ikke penge på denne model, og vi håber, at den kan bruges til at forbedre menneskelig kreativitet.
- **Brug & Attribution**: 
    - Vi opfordrer kunstnere og indholdsskabere til frit at inkorporere outputs genereret af DAVMusic i deres egne værker, inklusive kommercielle projekter. 
    - Vi opfordrer til attribution til modellens navn (“**DAVMusic by Nicklas**”), især til offentlig og kommerciel brug. 
- **Originalitet & Plagiat**: Det er udelukkende skabernes ansvar at sikre, at deres værker, afledt fra eller inspireret af DAVMusic outputs, ikke plagierer eller ulovligt reproducerer eksisterende materiale. Vi opfordrer stærkt brugere til at udføre deres egen due diligence for at undgå copyright-krænkelser eller andre juridiske overtrædelser.
- **Anbefalet mærkning**: Når du uploader værker til streamingplatforme eller deler dem offentligt, **anbefaler** vi at mærke dem med termer som: “AI-generated”, “DAVMusic-generated", “AI-assisted” eller “AI-auxiliated”. Dette hjælper med at opretholde transparens om den kreative proces.
- **Ansvarsfraskrivelse**: 
    - Vi påtager os intet ansvar for misbrug af denne model, inklusive (men ikke begrænset til) ulovlige, ondsindede eller uetiske aktiviteter. 
    - Brugere er eneansvarlige for alt indhold genereret ved hjælp af DAVMusic modellen og for eventuelle konsekvenser deraf.
    - Ved at bruge denne model accepterer du, at du forstår og overholder alle gældende love og reguleringer vedrørende dit genererede indhold.

---

## Acknowledgements
Projektet er tilpasset fra det originale YuE-projekt af multimodal-art-projection. Originalt co-ledet af HKUST og M-A-P (alfabetisk rækkefølge). Tak også til moonshot.ai, bytedance, 01.ai og geely for at støtte det originale projekt.
Et venligt link til original HKUST Audio group's [huggingface space](https://huggingface.co/HKUSTAudio). 

Vi sætter stor pris på al den støtte, vi har modtaget undervejs. Længe leve open-source AI!

---

## Citation

Hvis du finder vores (tilpassede) paper og kode nyttig i din forskning, overvej venligst at give en stjerne :star: og citation :pencil: :)

```BibTeX
@misc{nicklas2025davmusicscalingopenfoundation,
      title={DAVMusic: Scaling Open Foundation Models for Long-Form Music Generation}, 
      author={Nicklas og bidragydere (baseret på original YuE arbejde af Ruibin Yuan et al.)},
      year={2025},
      eprint={2503.08638},
      archivePrefix={arXiv},
      primaryClass={eess.AS},
      url={https://arxiv.org/abs/2503.08638}, 
}

@misc{nicklas2025davmusic,
  title={DAVMusic: Open Music Foundation Models for Full-Song Generation},
  author={Nicklas og bidragydere}, 
  howpublished={\url{https://github.com/cptleftnut/DAVMusic}},
  year={2025},
  note={GitHub repository, adapted from YuE by multimodal-art-projection}
}
```
<br>
