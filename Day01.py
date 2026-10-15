from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_DIR = Path("output/pdf")
PDF_NAME = "UGC_NET_CS_Word_Format_BW_Guide.pdf"


SOURCES = [
    (
        "NTA Information Bulletin, June 2025",
        "Confirms subject code 87 and official syllabus download route.",
        "https://ugcnet.nta.ac.in/images/information-bulletin-for-ugc-net-june-2025-16042025.pdf",
    ),
    (
        "UGC NET Computer Science and Applications Syllabus",
        "Official unit-wise syllabus used as the base structure.",
        "https://www.ugc-net.com/NTA_All_R_Syllabus/87/Computer%20Science%20and%20Applications_English%20Only.pdf",
    ),
    (
        "SamagraCS December 2025 Analysis",
        "Topic-level trend check for recent UGC NET CS paper.",
        "https://samagracs.com/ugc-net-computer-science-exam-analysis/",
    ),
    (
        "SamagraCS 2020-2018 Question Analysis",
        "Older cycle topic distribution used for long-term pattern cross-checking.",
        "https://samagracs.com/ugc-net-computer-science-previous-year-question-analysis-2020-2019-2018/",
    ),
    (
        "CollegeDekho Topic-Wise Weightage",
        "Cross-platform trend view for high, medium and low priority topics.",
        "https://www.collegedekho.com/articles/ugc-net-computer-science-topic-wise-weightage-analysis/",
    ),
    (
        "Testbook PYQ Page",
        "Year-wise paper availability and PYQ practice guidance.",
        "https://testbook.com/ugc-net/computer-science-and-applications-previous-year-question-papers?language=hindi",
    ),
    (
        "JRFAdda PYQ Download Index",
        "Cross-check for 2012-2025 paper availability and practice emphasis.",
        "https://www.jrfadda.com/exams/ugc-net/ugc-net-computer-science-previous-year-question-papers-download-pdfs/",
    ),
]


UNITS = [
    {
        "unit": "Unit 1",
        "name": "Discrete Structures and Optimization",
        "priority": "HIGH",
        "why": "Logic, relations, graph theory and optimization appear as concept/numerical questions.",
        "must_do": [
            "Propositional and predicate logic, CNF/DNF, quantifiers, inference rules",
            "Equivalence relation, partial order, Hasse diagram, lattice basics",
            "Graph coloring, planar graph, Euler formula, trees and spanning trees",
            "LPP formulation, duality, simplex idea, PERT-CPM, Hungarian method",
        ],
        "pyq": [
            "Find whether a logical statement is tautology/contradiction/contingency.",
            "Draw/read a Hasse diagram and identify maximal/minimal elements.",
            "Use Euler formula to test a planar graph or compute regions.",
            "Calculate critical path, slack or project duration from a PERT network.",
        ],
    },
    {
        "unit": "Unit 2",
        "name": "Computer System Architecture",
        "priority": "HIGH",
        "why": "Memory, cache, pipeline and addressing mode numericals repeat frequently.",
        "must_do": [
            "Number representation, 2's complement, IEEE 754 floating point",
            "Combinational/sequential circuits, flip-flops, counters, K-map",
            "Instruction formats, addressing modes, pipelining, hazards, speedup",
            "Cache mapping, average memory access time, TLB, virtual memory",
        ],
        "pyq": [
            "Compute cache tag/index/offset bits for direct or set associative mapping.",
            "Calculate pipeline speedup, latency or throughput with stalls.",
            "Convert a decimal value to IEEE 754 representation or 2's complement.",
            "Identify addressing mode used by a given instruction.",
        ],
    },
    {
        "unit": "Unit 3",
        "name": "Programming Languages and Computer Graphics",
        "priority": "MEDIUM",
        "why": "Usually mixed: output tracing, OOP concepts and graphics transformations.",
        "must_do": [
            "C/C++ pointer/output tracing, recursion, parameter passing",
            "OOP: inheritance, polymorphism, virtual functions, exceptions",
            "2D/3D transformations, homogeneous coordinates, viewing pipeline",
            "Line clipping, polygon clipping, Bezier curves, shading models",
        ],
        "pyq": [
            "Predict output of pointer/recursion based C/C++ code.",
            "Choose correct OOP concept for overloading/overriding/virtual call.",
            "Apply rotation/scaling/translation matrix to a point.",
            "Find line accept/reject result using Cohen-Sutherland clipping.",
        ],
    },
    {
        "unit": "Unit 4",
        "name": "Database Management Systems",
        "priority": "VERY HIGH",
        "why": "SQL, keys, normalization, transactions and indexing are among the most scoring areas.",
        "must_do": [
            "ER/EER model, relational model, relational algebra, tuple/domain calculus",
            "SQL joins, nested queries, grouping, constraints and views",
            "Functional dependency, closure, candidate key, 3NF, BCNF, lossless join",
            "Transactions, conflict serializability, 2PL, deadlock, B/B+ tree indexing",
        ],
        "pyq": [
            "Find candidate keys and normal form from a set of functional dependencies.",
            "Convert ER/EER relationship constraints into relational tables.",
            "Check conflict serializability using precedence graph.",
            "Write/evaluate SQL query using join, group by, having or nested condition.",
        ],
    },
    {
        "unit": "Unit 5",
        "name": "System Software and Operating System",
        "priority": "VERY HIGH",
        "why": "Scheduling, deadlock, paging and disk scheduling are regular numerical zones.",
        "must_do": [
            "Assembler/linker/loader basics, macro processing, compilers overview",
            "CPU scheduling: FCFS, SJF, SRTF, Priority, Round Robin",
            "Process synchronization, semaphores, monitors, deadlock, Banker's algorithm",
            "Paging, segmentation, page replacement, disk scheduling, file systems",
        ],
        "pyq": [
            "Draw Gantt chart and compute average waiting/turnaround time.",
            "Apply Banker's algorithm to decide safe/unsafe state.",
            "Count page faults using FIFO, LRU or Optimal replacement.",
            "Calculate total head movement for SCAN, C-SCAN, LOOK or SSTF.",
        ],
    },
    {
        "unit": "Unit 6",
        "name": "Software Engineering",
        "priority": "MEDIUM",
        "why": "Theory-heavy but predictable; useful for quick marks after core subjects.",
        "must_do": [
            "SDLC models: waterfall, spiral, incremental, agile, scrum",
            "SRS, use case, design principles, cohesion, coupling, UML basics",
            "LOC/FP estimation, COCOMO, project scheduling",
            "Testing: white-box, black-box, basis path, boundary value, regression",
        ],
        "pyq": [
            "Identify the correct SDLC model from given project conditions.",
            "Rank cohesion/coupling types or choose best design quality.",
            "Compute cyclomatic complexity from a control-flow graph.",
            "Estimate effort/time using basic COCOMO or function point data.",
        ],
    },
    {
        "unit": "Unit 7",
        "name": "Data Structures and Algorithms",
        "priority": "VERY HIGH",
        "why": "Trees, graphs, complexity and design techniques are consistently high-yield.",
        "must_do": [
            "Stacks, queues, linked lists, trees, BST/AVL/B/B+ tree, heap, hashing",
            "Sorting/searching, asymptotic notation, recurrence, Master theorem",
            "Divide and conquer, greedy, dynamic programming, backtracking, branch-bound",
            "BFS/DFS, shortest path, MST, max flow, NP-completeness",
        ],
        "pyq": [
            "Solve recurrence and classify time complexity.",
            "Perform AVL rotation/BST traversal/heap insertion or deletion.",
            "Trace BFS/DFS, Dijkstra, Prim or Kruskal on a graph.",
            "Identify P, NP, NP-complete or reducibility statement.",
        ],
    },
    {
        "unit": "Unit 8",
        "name": "Theory of Computation and Compilers",
        "priority": "VERY HIGH",
        "why": "TOC is concept dense; compilers add repeated parser and grammar questions.",
        "must_do": [
            "DFA/NFA conversion, regular expression, closure properties, pumping lemma",
            "CFG, PDA, ambiguity, CNF/GNF, Chomsky hierarchy",
            "Turing machine, decidability, halting problem, recursive/RE languages",
            "First/Follow, LL(1), LR/LALR parsing, syntax directed translation, optimization",
        ],
        "pyq": [
            "Convert NFA to DFA or minimize a DFA.",
            "Check whether a language is regular/CFL/decidable.",
            "Compute First and Follow sets and test LL(1) grammar.",
            "Identify shift-reduce/reduce-reduce conflict in LR parsing table.",
        ],
    },
    {
        "unit": "Unit 9",
        "name": "Data Communication and Computer Networks",
        "priority": "VERY HIGH",
        "why": "Subnetting, protocols, routing, TCP and security repeatedly appear.",
        "must_do": [
            "OSI/TCP-IP layers, framing, flow/error control, sliding window",
            "IPv4 addressing, CIDR, subnetting, fragmentation, ARP, routing",
            "TCP/UDP, congestion control, DNS, email protocols, FTP/TELNET",
            "Cryptography, RSA, digital signature, firewall, mobile networks, cloud/IoT basics",
        ],
        "pyq": [
            "Calculate subnet mask, usable hosts or network address from CIDR.",
            "Find sliding window efficiency or required sequence number bits.",
            "Compute CRC/checksum or identify error detection method.",
            "Match protocol to OSI/TCP-IP layer or port/service.",
        ],
    },
    {
        "unit": "Unit 10",
        "name": "Artificial Intelligence",
        "priority": "HIGH",
        "why": "Recent papers show strong emphasis on search, ML basics, KR and fuzzy/GA/ANN.",
        "must_do": [
            "State-space search, heuristic search, A*, AO*, game playing, alpha-beta",
            "Knowledge representation, inference, semantic nets, frames, expert systems",
            "Planning, NLP basics, multi-agent systems, semantic web",
            "Fuzzy sets, genetic algorithms, ANN: perceptron, MLP, SOM, Hopfield",
        ],
        "pyq": [
            "Check admissibility/optimality of A* heuristic.",
            "Apply minimax or alpha-beta pruning on a game tree.",
            "Perform fuzzy union/intersection/composition or defuzzification.",
            "Identify learning type or activation condition in ANN/perceptron.",
        ],
    },
]


def p(text, style):
    return Paragraph(text, style)


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.black)
    canvas.drawString(25 * mm, 13 * mm, "UGC NET CS - Word Format High-Yield Guide")
    canvas.drawRightString(185 * mm, 13 * mm, f"Page {doc.page}")
    canvas.restoreState()


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=31,
            alignment=TA_CENTER,
            textColor=colors.black,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=13,
            leading=18,
            alignment=TA_CENTER,
            textColor=colors.black,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1BW",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=22,
            textColor=colors.black,
            spaceBefore=8,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2BW",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=colors.black,
            spaceBefore=6,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyBW",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            textColor=colors.black,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallBW",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=13.5,
            textColor=colors.black,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TinyBW",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor=colors.black,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CellHead",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=14,
            textColor=colors.black,
        )
    )
    return styles


def priority_style(priority):
    if priority == "VERY HIGH":
        return colors.HexColor("#BFBFBF"), colors.black
    if priority == "HIGH":
        return colors.HexColor("#D9D9D9"), colors.black
    return colors.white, colors.black


def source_note():
    return (
        "Research base: official UGC/NTA syllabus plus cross-check from public PYQ/trend "
        "platforms. Exact papers vary by year and shift; the PYQ section below lists repeated "
        "question patterns and rephrased practice prompts from the last 10-year trend."
    )


def add_cover(story, styles):
    story.append(Spacer(1, 20 * mm))
    story.append(p("UGC NET Computer Science and Applications", styles["CoverTitle"]))
    story.append(p("Subject Code 87", styles["CoverSub"]))
    story.append(p("Black and White Word-Style Study PDF", styles["CoverSub"]))
    story.append(p("Syllabus + Important Topics + Last 10-Year PYQ Pattern", styles["CoverSub"]))
    story.append(Spacer(1, 12 * mm))

    legend = [
        [p("<b>Priority</b>", styles["BodyBW"]), p("<b>Meaning</b>", styles["BodyBW"])],
        [p("VERY HIGH", styles["BodyBW"]), p("Do first. Maximum PYQ value and scoring potential.", styles["BodyBW"])],
        [p("HIGH", styles["BodyBW"]), p("Do next. Regularly asked and concept-heavy.", styles["BodyBW"])],
        [p("MEDIUM", styles["BodyBW"]), p("Quick revision + selective depth after core topics.", styles["BodyBW"])],
    ]
    table = Table(legend, colWidths=[42 * mm, 116 * mm], hAlign="CENTER")
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E6E6E6")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 10 * mm))
    story.append(p(source_note(), styles["BodyBW"]))
    story.append(Spacer(1, 8 * mm))
    story.append(
        p(
            "<b>Best order:</b> Unit 7, Unit 5, Unit 4, Unit 9, Unit 8, Unit 1, Unit 10, Unit 2, Unit 6, Unit 3.",
            styles["BodyBW"],
        )
    )
    story.append(PageBreak())


def add_snapshot(story, styles):
    story.append(p("Priority Snapshot", styles["H1BW"]))
    data = [[p("<b>Rank</b>", styles["SmallBW"]), p("<b>Unit</b>", styles["SmallBW"]), p("<b>Main Focus</b>", styles["SmallBW"])]]
    ordered = [
        ("1", "Unit 7 - DSA", "Trees, graphs, recurrence, DP/greedy, complexity"),
        ("2", "Unit 5 - OS", "Scheduling, deadlock, paging, page replacement, disk scheduling"),
        ("3", "Unit 4 - DBMS", "SQL, keys, normalization, serializability, indexing"),
        ("4", "Unit 9 - Networks", "CIDR, sliding window, TCP, OSI/TCP-IP, security"),
        ("5", "Unit 8 - TOC/Compiler", "DFA/NFA, CFL, decidability, First/Follow, LR parsing"),
        ("6", "Unit 1 - Discrete/Optimization", "Logic, relation, graph, LPP, PERT-CPM"),
        ("7", "Unit 10 - AI", "A*, minimax, KR, fuzzy, GA, ANN"),
        ("8", "Unit 2 - COA", "Cache, pipeline, addressing, number representation"),
        ("9", "Unit 6 - SE", "Models, testing, cohesion/coupling, COCOMO"),
        ("10", "Unit 3 - PL/Graphics", "Output tracing, OOP, transformations, clipping"),
    ]
    for row in ordered:
        data.append([p(row[0], styles["SmallBW"]), p(row[1], styles["SmallBW"]), p(row[2], styles["SmallBW"])])

    table = Table(data, colWidths=[18 * mm, 50 * mm, 92 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9D9D9")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 6 * mm))
    story.append(
        p(
            "<b>Rule:</b> VERY HIGH topics need concept notes + PYQs + timed practice. MEDIUM topics can be revised through short notes and direct MCQs.",
            styles["BodyBW"],
        )
    )
    story.append(PageBreak())


def unit_block(unit, styles):
    bg, text = priority_style(unit["priority"])
    header = Table(
        [
            [
                p(f"<b>{unit['unit']}: {unit['name']}</b>", styles["BodyBW"]),
                p(f"<b>{unit['priority']}</b>", styles["BodyBW"]),
            ]
        ],
        colWidths=[118 * mm, 42 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
                ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#E6E6E6")),
                ("BACKGROUND", (1, 0), (1, 0), bg),
                ("TEXTCOLOR", (1, 0), (1, 0), text),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (1, 0), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )

    must_do = "<br/>".join(f"- <b>{item}</b>" if i < 2 else f"- {item}" for i, item in enumerate(unit["must_do"]))
    pyq = "<br/>".join(f"- {item}" for item in unit["pyq"])
    body = Table(
        [
            [p("Why important", styles["CellHead"]), p(unit["why"], styles["SmallBW"])],
            [p("Important topics", styles["CellHead"]), p(must_do, styles["SmallBW"])],
            [p("Last 10-year PYQ pattern", styles["CellHead"]), p(pyq, styles["SmallBW"])],
        ],
        colWidths=[42 * mm, 118 * mm],
    )
    body.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.6, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.black),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F2F2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return KeepTogether([header, body, Spacer(1, 9 * mm)])


def add_units(story, styles):
    story.append(p("Unit-Wise High-Yield Notes", styles["H1BW"]))
    story.append(p("Bold lines are the first topics to revise. Each unit is kept in a Word-style table with bullet points.", styles["BodyBW"]))
    story.append(Spacer(1, 5 * mm))
    for unit in UNITS:
        story.append(unit_block(unit, styles))


def add_roadmap(story, styles):
    story.append(p("30-Day Revision Roadmap", styles["H1BW"]))
    roadmap = [
        ("Day 1-7", "DSA + OS", "Daily numericals: recurrence, graph algorithms, scheduling, paging."),
        ("Day 8-13", "DBMS + Networks", "SQL/FD/normalization + subnetting/sliding window/TCP."),
        ("Day 14-19", "TOC/Compiler + Discrete", "Automata, decidability, First/Follow, graph theory, PERT-CPM."),
        ("Day 20-24", "COA + AI", "Cache, pipeline, A*, minimax, fuzzy, ANN, GA."),
        ("Day 25-27", "SE + PL/Graphics", "Testing, COCOMO, output tracing, transformations, clipping."),
        ("Day 28-30", "PYQ Marathon", "Attempt 3 full previous papers and make error notebook."),
    ]
    data = [[p("<b>Days</b>", styles["SmallBW"]), p("<b>Subject</b>", styles["SmallBW"]), p("<b>Work</b>", styles["SmallBW"])]]
    for row in roadmap:
        data.append([p(row[0], styles["SmallBW"]), p(row[1], styles["SmallBW"]), p(row[2], styles["SmallBW"])])
    table = Table(data, colWidths=[28 * mm, 45 * mm, 87 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9D9D9")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)


def add_sources(story, styles):
    story.append(Spacer(1, 7 * mm))
    story.append(p("Research Sources Checked", styles["H1BW"]))
    rows = [[p("<b>Source</b>", styles["TinyBW"]), p("<b>Used for</b>", styles["TinyBW"]), p("<b>URL</b>", styles["TinyBW"])]]
    for name, used_for, url in SOURCES:
        rows.append([p(name, styles["TinyBW"]), p(used_for, styles["TinyBW"]), p(url, styles["TinyBW"])])
    table = Table(rows, colWidths=[43 * mm, 53 * mm, 64 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.7, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E6E6E6")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(table)


def create_ugc_net_pdf(filename=None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = Path(filename) if filename else OUTPUT_DIR / PDF_NAME
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=25 * mm,
        leftMargin=25 * mm,
        topMargin=22 * mm,
        bottomMargin=22 * mm,
        title="UGC NET CS Word Format Black and White Guide",
        author="Generated from Day01.py",
    )
    story = []
    add_cover(story, styles)
    add_snapshot(story, styles)
    add_units(story, styles)
    add_roadmap(story, styles)
    add_sources(story, styles)
    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    print(f"PDF generated successfully: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    create_ugc_net_pdf()
