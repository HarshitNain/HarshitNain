"""
Verified, hand-curated facts for the profile dashboard.
"""

OWNER = "abhi5heksah"
NAME = "Abhishek Kumar Sah"
TAGLINE = "Full Stack Developer (MERN & React Native)"
SUBLINE = "I build responsive, scalable, and user-friendly interfaces with modern web technologies."

# ---------------------------------------------------------------------------
# The flagship portfolio.
# ---------------------------------------------------------------------------
FLAGSHIPS = [
    # Full Stack Development
    dict(name="parlour-booking-system", domain="Full Stack Development", lang="JavaScript", tag="v1.0.0",
         blurb="Complete Parlour Booking System with online service booking, dynamic discount management, and Google SSO authentication."),
    dict(name="mern-ecommerce", domain="Full Stack Development", lang="TypeScript", tag=None,
         blurb="Scalable full-stack e-commerce application using React.js, Node.js, and MongoDB with optimized structured schema design."),
    
    # Frontend & UI
    dict(name="admin-dashboard-pro", domain="Frontend & UI", lang="TypeScript", tag="v2.1",
         blurb="Dedicated Admin Dashboard for administrative control, booking approval workflows, and service configuration using React, ShadCN, and GSAP."),
    dict(name="modern-portfolio", domain="Frontend & UI", lang="JavaScript", tag=None,
         blurb="Highly interactive portfolio built with modern UI systems using Tailwind CSS, ShadCN UI, and micro-animations."),
    
    # Backend & APIs
    dict(name="rnr-microservices", domain="Backend & APIs", lang="JavaScript", tag=None, private=True,
         blurb="Production-ready internal platforms and client-facing systems using robust REST APIs and modular architecture."),
    dict(name="puja-backend", domain="Backend & APIs", lang="TypeScript", tag=None,
         blurb="Secure NestJS backend API for Beauty Parlour management, featuring Google OAuth, Prisma ORM, and Razorpay integration."),
    
    # Security
    dict(name="CompliSec", domain="Security", lang="Python", tag="v0.1.0",
         blurb="Automated Vulnerability Scanning Tool integrated with Nmap, OpenVAS, and Nikto for port scanning and vulnerability identification."),
    
    # Mobile Development
    dict(name="react-native-companion", domain="Mobile Development", lang="TypeScript", tag=None,
         blurb="Cross-platform mobile companion app built with React Native for seamless user experience across iOS and Android."),
    dict(name="flutter-ui-kit", domain="Mobile Development", lang="Dart", tag=None,
         blurb="Collection of reusable, performant Flutter components and responsive layouts for mobile applications."),
]

DOMAINS = [
    "Full Stack Development",
    "Frontend & UI",
    "Backend & APIs",
    "Security",
    "Mobile Development",
]

# ---------------------------------------------------------------------------
# Verified benchmark numbers.
# ---------------------------------------------------------------------------
BENCHMARKS = [
    dict(repo="parlour-booking-system", metric="lighthouse performance",
         value="98/100", detail="Optimized React rendering & GSAP animations",
         env="Vercel · Chrome Desktop · 2026-07-21", source="lighthouse-report.json",
         bar=0.98),
    dict(repo="CompliSec", metric="scan coverage",
         value="10,000+", detail="Ports and services scanned accurately with Nmap/Nikto",
         env="Kali Linux · Local Network · 2025", source="reports/summary.md",
         bar=0.95),
    dict(repo="mern-ecommerce", metric="api response time",
         value="~45 ms", detail="Optimized MongoDB aggregations & Express middleware",
         env="Node v20 · AWS EC2 · 2026", source="tests/load-test.yml",
         bar=0.15),
    dict(repo="react-native-companion", metric="bundle size",
         value="< 15 MB", detail="Hermes engine enabled, optimized assets and code splitting",
         env="Expo EAS Build · Android APK", source="eas.json",
         bar=None), 
]

# ---------------------------------------------------------------------------
# Regulatory / Roadmap Deadlines
# ---------------------------------------------------------------------------
PQC_DEADLINES = [
    dict(date="2026-10-01", label="Frontend Migration",
         note="Upgrade all legacy React apps to React 19 and Next.js 15"),
    dict(date="2027-02-01", label="Mobile Excellence",
         note="Publish full React Native and Flutter UI kits to open source"),
    dict(date="2028-01-01", label="System Architecture",
         note="Master microservices and scalable cloud deployments (AWS/Docker)"),
    dict(date="2030-01-01", label="Full Stack Master",
         note="Architect enterprise-grade MERN + Mobile systems globally"),
]

# GitHub linguist colors
LANG_COLORS = {
    "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "Python": "#3572A5",
    "Dart": "#00B4AB", "HTML": "#e34c26", "CSS": "#563d7c", "Go": "#00ADD8",
    "Java": "#b07219", "Shell": "#89e051"
}

# ===========================================================================
# Real professional background
# ===========================================================================

JOURNEY_ERAS = [
    dict(key="2020", label="FOUNDATIONS", accent="cyan",
         note="B.Tech CS begins — The software engineering journey starts"),
    dict(key="2022", label="FIRST BUILDS", accent="blue",
         note="Learning HTML, CSS, JavaScript, and building early UIs"),
    dict(key="2024", label="MERN STACK", accent="purple",
         note="Mastering React, Node.js, and completing certifications"),
    dict(key="2025", label="BUILD & SHIP", accent="orange",
         note="Hackathons, CompliSec, Parlour Booking System & Internship"),
    dict(key="2026", label="FULL STACK PRO", accent="red",
         note="Working as Full Stack Developer at RnR Consulting"),
]

JOURNEY_MILES = [
    dict(date="2020-05", label="Class XII", sub="Ram Krishna College", lane="down", accent="cyan"),
    dict(date="2020-09", label="B.Tech CS begins", sub="Gandhi Engineering College", lane="down", accent="cyan"),
    dict(date="2022-11", label="First UIs", sub="Learning HTML/CSS/JS", lane="up", accent="blue"),
    dict(date="2024-03", label="Web Dev Cert", sub="Internshala MERN Stack", lane="down", accent="purple"),
    dict(date="2024-05", label="SQL Cert", sub="HackerRank SQL Expert", lane="down", accent="purple"),
    dict(date="2024-11", label="Codesquadz Intern", sub="MERN Stack Developer", lane="up", accent="orange"),
    dict(date="2025-01", label="Parlour System", sub="React & Node.js platform", lane="up", accent="orange"),
    dict(date="2025-03", label="Yukti Sangam", sub="Hackathon 2025 Participant", lane="down", accent="orange"),
    dict(date="2025-04", label="CompliSec", sub="Automated Vuln Scanner", lane="up", accent="orange"),
    dict(date="2025-05", label="Full Stack Dev", sub="RnR Consulting", lane="up", accent="red"),
    dict(date="2026-06", label="React Native", sub="Mobile Development", lane="up", accent="red"),
]

PUBLICATIONS = dict(
    counts=[("2+", "YEARS", "Experience"),
            ("10+", "PROJECTS", "Full Stack & Mobile"),
            ("2", "CERTIFICATIONS", "2024")],
    venues=[
        "Full Stack Developer @ RnR Consulting Private Limited (Apr 2025 - Present)",
        "MERN Stack Developer Intern @ Codesquadz, Noida (Nov 2024 - Apr 2025)",
        "Yukti Sangam Hackathon 2025 Participant - Built CompliSec",
        "Certifications: Web Development (Internshala), SQL (HackerRank)"
    ],
)

IMPACT = [
    ("100%", "Responsive UI", "Tailwind CSS, ShadCN UI, Material UI and Bootstrap"),
    ("REST", "API Integration", "Secure client-server communication and dynamic data flow"),
    ("NoSQL/SQL", "Database Design", "MongoDB and MySQL optimized CRUD operations"),
    ("SSO", "Authentication", "Google SSO and secure token-based user login workflows"),
]

EARLIER = [
    dict(name="Old-Portfolio", year="2023", lang="HTML/CSS",
         blurb="Early version of my portfolio built with pure HTML, CSS, and Bootstrap."),
    dict(name="Basic-CRUD-App", year="2024", lang="JavaScript",
         blurb="A simple CRUD application to master RESTful APIs using Express.js and MongoDB."),
]

CAREER_LINE = "Full Stack Developer @ RnR Consulting · B.Tech CS — Gandhi Engineering College, 2020–24"
