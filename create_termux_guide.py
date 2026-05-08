#!/usr/bin/env python3
"""
DAVMusic - Grafisk vejledning til Android + Termux
Genererer en professionel PDF-manual på dansk.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white, grey
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, ListFlowable, ListItem, KeepTogether, Image
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

# Farver
PRIMARY_COLOR = HexColor("#1a73e8")      # Google blå
WARNING_COLOR = HexColor("#d93025")      # Rød
SUCCESS_COLOR = HexColor("#34a853")      # Grøn
BG_LIGHT = HexColor("#f8f9fa")
CODE_BG = HexColor("#f1f3f4")

def create_styles():
    styles = getSampleStyleSheet()
    
    # Titel stil
    styles.add(ParagraphStyle(
        name='MainTitle',
        parent=styles['Title'],
        fontSize=28,
        textColor=PRIMARY_COLOR,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    # Undertitel
    styles.add(ParagraphStyle(
        name='SubTitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=grey,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    # Sektionsoverskrift
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=PRIMARY_COLOR,
        spaceBefore=20,
        spaceAfter=12,
        fontName='Helvetica-Bold',
        borderPadding=5,
    ))
    
    # Trin overskrift
    styles.add(ParagraphStyle(
        name='StepHeader',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor("#202124"),
        spaceBefore=15,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        leftIndent=0
    ))
    
    # Normal tekst
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    ))
    
    # Advarsel tekst
    styles.add(ParagraphStyle(
        name='WarningText',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        textColor=WARNING_COLOR,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    ))
    
    # Kode stil
    styles.add(ParagraphStyle(
        name='CustomCode',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Courier',
        leading=12,
        backColor=CODE_BG,
        leftIndent=10,
        rightIndent=10,
        spaceBefore=6,
        spaceAfter=6
    ))
    
    # Note / tip
    styles.add(ParagraphStyle(
        name='TipText',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=HexColor("#137333"),
        leftIndent=15,
        fontName='Helvetica-Oblique'
    ))
    
    return styles

def add_header_footer(canvas, doc):
    canvas.saveState()
    
    # Header
    canvas.setFillColor(PRIMARY_COLOR)
    canvas.rect(0, A4[1] - 1.5*cm, A4[0], 1.5*cm, fill=True, stroke=False)
    canvas.setFillColor(white)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(1.5*cm, A4[1] - 1*cm, "DAVMusic på Android – Termux Guide")
    
    # Footer
    canvas.setFillColor(grey)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(1.5*cm, 1*cm, "Nicklas / cptleftnut / DAVLm – 2026")
    canvas.drawRightString(A4[0] - 1.5*cm, 1*cm, f"Side {doc.page}")
    
    canvas.restoreState()

def create_warning_box(text, styles):
    """Opretter en advarselsboks"""
    data = [[Paragraph(f"<b>⚠️ VIGTIG ADVARSEL</b><br/><br/>{text}", styles['CustomBody'])]]
    t = Table(data, colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#fce8e6")),
        ('BOX', (0, 0), (-1, -1), 2, WARNING_COLOR),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    return t

def create_tip_box(text, styles):
    """Opretter en tip-boks"""
    data = [[Paragraph(f"<b>💡 TIP:</b> {text}", styles['TipText'])]]
    t = Table(data, colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#e6f4ea")),
        ('BOX', (0, 0), (-1, -1), 1, SUCCESS_COLOR),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    return t

def create_code_block(code_text, styles):
    """Opretter en kodeblok"""
    return Paragraph(f"<font face='Courier' size='9'>{code_text}</font>", styles['CustomCode'])

def build_manual():
    output_path = "/home/workdir/artifacts/DAVMusic/DAVMusic_Termux_Guide_Danish.pdf"
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm
    )
    
    styles = create_styles()
    story = []
    
    # ========== TITELSIDE ==========
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("DAVMusic", styles['MainTitle']))
    story.append(Paragraph("Installation & Opsætning på Android", styles['SubTitle']))
    story.append(Paragraph("Trin-for-trin grafisk guide med Termux<br/>(uden root-adgang)", styles['SubTitle']))
    story.append(Spacer(1, 1*cm))
    
    # Info boks
    info_data = [[Paragraph(
        "<b>Version:</b> 1.0 &nbsp;&nbsp;|&nbsp;&nbsp; <b>Forfatter:</b> Nicklas (cptleftnut / DAVLm)<br/>"
        "<b>Model:</b> m-a-p/YuE-s1-7B-anneal-en-cot<br/>"
        "<b>Dato:</b> Maj 2026",
        styles['CustomBody']
    )]]
    info_table = Table(info_data, colWidths=[14*cm])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1, PRIMARY_COLOR),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(info_table)
    
    story.append(PageBreak())
    
    # ========== INDHOLDSFORTEGNELSE ==========
    story.append(Paragraph("Indholdsfortegnelse", styles['SectionHeader']))
    toc_items = [
        "1. Vigtige advarsler før du starter",
        "2. Forudsætninger",
        "3. Trin 1: Installation af Termux",
        "4. Trin 2: Opdatering og grundlæggende pakker",
        "5. Trin 3: Installation af Python-miljø",
        "6. Trin 4: Opsætning af DAVMusic",
        "7. Trin 5: Kørsel af generate.py",
        "8. Realistiske forventninger & begrænsninger",
        "9. Fejlfinding",
        "10. Anbefalede alternativer"
    ]
    for item in toc_items:
        story.append(Paragraph(item, styles['CustomBody']))
    story.append(Spacer(1, 0.5*cm))
    
    # ========== 1. VIGTIGE ADVARSLER ==========
    story.append(Paragraph("1. Vigtige advarsler før du starter", styles['SectionHeader']))
    
    story.append(create_warning_box(
        "Dette setup er <b>teknisk meget udfordrende</b> på en almindelig Android-telefon. "
        "YuE-modellen (7B + 1B parametre) kræver normalt minimum 24 GB VRAM og 32+ GB RAM for at køre komfortabelt. "
        "De fleste Android-telefoner har kun 6–16 GB RAM i alt (delt med systemet). "
        "<br/><br/>"
        "<b>Realistisk resultat:</b> Du vil sandsynligvis opleve:<br/>"
        "• Out-of-Memory (OOM) fejl under modelindlæsning<br/>"
        "• Ekstremt langsom generering (timer pr. sang)<br/>"
        "• App-crash eller Termux der lukker<br/><br/>"
        "Denne guide hjælper dig så langt som muligt, men forvent ikke fuld funktionalitet på telefonen.",
        styles
    ))
    
    story.append(Spacer(1, 0.4*cm))
    story.append(create_tip_box(
        "Hvis du primært vil generere musik, anbefales det stærkt at bruge Google Colab (gratis GPU), "
        "RunPod, Vast.ai eller en lille cloud-server i stedet for lokal kørsel på telefonen.",
        styles
    ))
    
    # ========== 2. FORUDSÆTNINGER ==========
    story.append(Paragraph("2. Forudsætninger", styles['SectionHeader']))
    story.append(Paragraph(
        "Før du går i gang, skal du have følgende klar:",
        styles['CustomBody']
    ))
    
    prereqs = [
        "En Android-telefon med mindst 8 GB RAM (12 GB+ anbefales)",
        "Termux installeret fra F-Droid (ikke Google Play – den er forældet)",
        "God internetforbindelse (modellen er flere GB stor)",
        "Tålmodighed – installationen tager 30–90 minutter",
        "Plads på telefonen: mindst 15–20 GB ledig lager"
    ]
    for p in prereqs:
        story.append(Paragraph(f"• {p}", styles['CustomBody']))
    
    story.append(PageBreak())
    
    # ========== 3. TRIN 1: INSTALLATION AF TERMUX ==========
    story.append(Paragraph("3. Trin 1: Installation af Termux", styles['SectionHeader']))
    
    story.append(Paragraph("<b>Trin 1.1 – Download Termux</b>", styles['StepHeader']))
    story.append(Paragraph(
        "Gå til <b>F-Droid</b> (https://f-droid.org) og søg efter <b>Termux</b>. "
        "Installer den nyeste version. <b>Undgå</b> versionen fra Google Play Store, da den er forældet og ikke understøttes længere.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("<b>Trin 1.2 – Første start af Termux</b>", styles['StepHeader']))
    story.append(Paragraph(
        "Åbn Termux. Du vil se en sort terminal med en prompt der ligner:<br/>"
        "<font face='Courier'>$</font>",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "Hvis du får en fejl om \"package not found\" eller lignende, skal du følge instruktionerne på Termux' GitHub for at opdatere repositories.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("<b>Trin 1.3 – Giv tilladelser (vigtigt)</b>", styles['StepHeader']))
    story.append(Paragraph(
        "Kør følgende kommando for at give Termux adgang til lageret:",
        styles['CustomBody']
    ))
    story.append(create_code_block("termux-setup-storage", styles))
    story.append(Paragraph(
        "Tryk Enter. Accepter tilladelserne når Android spørger.",
        styles['CustomBody']
    ))
    
    # ========== 4. TRIN 2: OPDATERING ==========
    story.append(Paragraph("4. Trin 2: Opdatering og grundlæggende pakker", styles['SectionHeader']))
    
    story.append(Paragraph(
        "Opdater først Termux fuldstændigt:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "pkg update && pkg upgrade -y", styles
    ))
    
    story.append(Paragraph(
        "Installer nødvendige grundpakker:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "pkg install -y git python clang cmake ninja wget curl termux-api", styles
    ))
    
    story.append(create_tip_box(
        "Hvis en pakke fejler, prøv at køre `pkg update` igen og derefter installér pakken enkeltvis.",
        styles
    ))
    
    story.append(PageBreak())
    
    # ========== 5. TRIN 3: PYTHON MILJØ ==========
    story.append(Paragraph("5. Trin 3: Installation af Python-miljø", styles['SectionHeader']))
    
    story.append(Paragraph(
        "Vi opretter et virtuelt miljø for at undgå konflikter:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "python -m venv ~/davmusic-env\n"
        "source ~/davmusic-env/bin/activate", styles
    ))
    
    story.append(Paragraph(
        "Du skulle nu se <b>(davmusic-env)</b> foran prompten. Det betyder at miljøet er aktivt.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph(
        "Opgrader pip og installer grundlæggende pakker:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "pip install --upgrade pip wheel setuptools", styles
    ))
    
    story.append(Paragraph(
        "<b>Installer PyTorch (CPU-version – ingen CUDA på de fleste telefoner):</b>",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu", styles
    ))
    
    story.append(create_warning_box(
        "PyTorch med GPU-acceleration (CUDA) er ekstremt svært at få til at virke i Termux uden root og special-builds. "
        "CPU-versionen er det eneste realistiske valg på de fleste telefoner.",
        styles
    ))
    
    # ========== 6. TRIN 4: OPSÆTNING AF DAVMUSIC ==========
    story.append(Paragraph("6. Trin 4: Opsætning af DAVMusic", styles['SectionHeader']))
    
    story.append(Paragraph(
        "Klon dit repository:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "cd ~\n"
        "git clone https://github.com/cptleftnut/DAVMusic.git\n"
        "cd DAVMusic", styles
    ))
    
    story.append(Paragraph(
        "Installer krav fra requirements.txt (dette kan tage lang tid):",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "pip install -r requirements.txt", styles
    ))
    
    story.append(Paragraph(
        "Hvis du får fejl med FlashAttention eller andre pakker der kræver CUDA, kan du springe dem over eller installere CPU-alternativer. "
        "Mange afhængigheder vil fejle på grund af manglende GPU-support.",
        styles['CustomBody']
    ))
    
    story.append(create_tip_box(
        "Hvis installationen af en pakke fejler, kan du prøve at installere den med `--no-deps` eller springe den over og fortsætte.",
        styles
    ))
    
    story.append(PageBreak())
    
    # ========== 7. TRIN 5: KØRSEL ==========
    story.append(Paragraph("7. Trin 5: Kørsel af generate.py", styles['SectionHeader']))
    
    story.append(Paragraph(
        "Gå ind i inference-mappen og prøv scriptet:",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "cd inference\n"
        "python generate.py --help", styles
    ))
    
    story.append(Paragraph(
        "Prøv et meget lille test (1 segment, kort tekst):",
        styles['CustomBody']
    ))
    story.append(create_code_block(
        "python generate.py \\\n"
        "  --lyrics \"[verse] Test sangtekst her\" \\\n"
        "  --genre \"pop male vocal\" \\\n"
        "  --segments 1", styles
    ))
    
    story.append(create_warning_box(
        "På de fleste Android-telefoner vil dette enten:<br/>"
        "• Fejle med Out-of-Memory<br/>"
        "• Tage flere timer pr. segment<br/>"
        "• Få Termux til at lukke ned<br/><br/>"
        "Hvis det sker, er det forventet pga. hardware-begrænsninger.",
        styles
    ))
    
    # ========== 8. REALISTISKE FORVENTNINGER ==========
    story.append(Paragraph("8. Realistiske forventninger & begrænsninger", styles['SectionHeader']))
    
    story.append(Paragraph(
        "Her er en ærlig oversigt over hvad du kan forvente:",
        styles['CustomBody']
    ))
    
    # Tabel med forventninger
    table_data = [
        ['Handling', 'Forventet resultat på telefon'],
        ['Installation af Termux + pakker', 'Fungerer godt'],
        ['Installation af PyTorch (CPU)', 'Fungerer (langsomt)'],
        ['Download af 7B model', 'Muligt, men langsomt (flere GB)'],
        ['Kørsel af fuld sang (2+ segmenter)', 'Meget usandsynligt (OOM)'],
        ['Kørsel af 1 kort segment', 'Muligt på high-end telefoner, men langsomt'],
        ['Brug af FlashAttention 2', 'Fungerer ikke (kræver CUDA)'],
        ['Gradio web-UI', 'Svært at få til at køre stabilt'],
    ]
    
    t = Table(table_data, colWidths=[7*cm, 9*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, grey),
        ('BACKGROUND', (0, 1), (-1, -1), BG_LIGHT),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    
    story.append(PageBreak())
    
    # ========== 9. FEJLFINDING ==========
    story.append(Paragraph("9. Fejlfinding – Almindelige problemer", styles['SectionHeader']))
    
    problems = [
        ("<b>Fejl: Out of memory / Killed</b>", 
         "Luk alle andre apps. Prøv med `--segments 1` og meget kort tekst. Overvej cloud i stedet."),
        ("<b>pip install fejler på torch</b>", 
         "Brug den CPU-version der er angivet i guiden. Undgå CUDA-pakker."),
        ("<b>Termux lukker ned</b>", 
         "Telefonen har for lidt RAM. Genstart Termux og prøv igen med mindre belastning."),
        ("<b>Model download fejler</b>", 
         "Tjek internet og plads. Brug `huggingface-cli login` med dit token hvis nødvendigt."),
        ("<b>FlashAttention fejler</b>", 
         "Spring det over – det kræver CUDA som ikke er tilgængeligt på de fleste telefoner."),
    ]
    
    for title, solution in problems:
        story.append(Paragraph(title, styles['StepHeader']))
        story.append(Paragraph(solution, styles['CustomBody']))
    
    # ========== 10. ALTERNATIVER ==========
    story.append(Paragraph("10. Anbefalede alternativer (stærkt anbefalet)", styles['SectionHeader']))
    
    story.append(Paragraph(
        "I stedet for at kæmpe med Termux på telefonen, overvej disse meget bedre løsninger:",
        styles['CustomBody']
    ))
    
    alts = [
        "<b>Google Colab</b> – Gratis GPU (T4), nemt at køre YuE i en notebook. Mest anbefalet til begyndere.",
        "<b>RunPod / Vast.ai / Lambda Labs</b> – Billig GPU-leje (ca. 0,2–0,5 USD/time). Meget hurtigere end telefon.",
        "<b>En lille hjemmeserver / mini-PC</b> med RTX 3060 eller bedre – ideelt til lokal kørsel.",
        "<b>Termux + proot-distro</b> med Ubuntu + CUDA (avanceret, kræver ofte root eller speciel telefon).",
    ]
    for alt in alts:
        story.append(Paragraph(f"• {alt}", styles['CustomBody']))
    
    story.append(Spacer(1, 1*cm))
    
    # Afslutning
    story.append(Paragraph(
        "<b>Konklusion:</b> Du kan følge denne guide for at sætte miljøet op på din Android-telefon, "
        "men for at generere rigtig musik med YuE-modellen anbefales det kraftigt at bruge en cloud-løsning med rigtig GPU. "
        "Telefonen er primært nyttig til at teste små ting eller som fjernterminal til en cloud-server.",
        styles['CustomBody']
    ))
    
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(
        "Hvis du har spørgsmål eller brug for hjælp til en cloud-opsætning i stedet, er du velkommen til at spørge.",
        styles['CustomBody']
    ))
    
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph(
        "— Nicklas / cptleftnut / DAVLm",
        ParagraphStyle('Signature', parent=styles['CustomBody'], alignment=TA_CENTER, textColor=grey)
    ))
    
    # Byg PDF
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"PDF oprettet: {output_path}")
    return output_path

if __name__ == "__main__":
    build_manual()
