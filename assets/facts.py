"""
Verified, hand-curated facts for the profile dashboard.
"""

OWNER = "HarshitNain"
NAME = "Harshit Nain"
TAGLINE = "Full Stack Engineer & Backend Systems Architect"
SUBLINE = "Building scalable cloud platforms, resilient microservices, and high-performance modern web applications."

# ---------------------------------------------------------------------------
# The flagship portfolio.
# ---------------------------------------------------------------------------
FLAGSHIPS = [
    # Full Stack Development
    dict(name="NHIT-Digital-Platform", domain="Full Stack Development", lang="Go", tag="v1.2.0", private=False,
         blurb="The next-generation digital operating system for National Highways Infra Trust (NHIT). Automating green notes, Section 194C TDS, and direct banking reconciliation."),
    dict(name="Youtube-Clone", domain="Full Stack Development", lang="TypeScript", tag="v1.0.0", private=True,
         blurb="Feature-rich video streaming platform replica with dynamic video feeds, channel metrics, and responsive playback."),
    dict(name="B.Tech-CS----2022", domain="Full Stack Development", lang="Python", tag=None, private=False,
         blurb="Curated suite of final year Computer Science engineering capstones, distributed systems, and ML prototypes."),

    # Frontend & UI
    dict(name="Food-Delivery-Web-App", domain="Frontend & UI", lang="JavaScript", tag="v1.0.0", private=False,
         blurb="Full-featured Food Delivery Web App built with React.js, Redux Toolkit, Material UI, and Context API."),
    dict(name="Food-Villa", domain="Frontend & UI", lang="JavaScript", tag=None, private=False,
         blurb="Interactive restaurant discovery and online food ordering platform built with modern component architecture."),

    # Backend & APIs
    dict(name="Enterprise-SyncHub", domain="Backend & APIs", lang="Go", tag=None, private=True,
         blurb="High-concurrency synchronization gateway, distributed event bus, and persistent agent communication harness."),

    # Security
    dict(name="Secure-Gateway-Shield", domain="Security", lang="Go", tag="v1.0.0", private=True,
         blurb="Distributed memory OTP store, Google SSO token validation, secrets vault, and high-precision API rate limiting."),

    # Mobile Development
    dict(name="Food-Villa-Mobile", domain="Mobile Development", lang="JavaScript", tag=None, private=True,
         blurb="Cross-platform React Native companion app for seamless mobile food discovery and live order tracking."),
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
    dict(repo="NHIT-Digital-Platform", metric="api response time",
         value="< 45 ms", detail="Optimized Go microservices, distributed caching & PostgreSQL indexing",
         env="Go 1.22 · AWS Cloud · 2026", source="tests/load-test.yml",
         bar=0.15),
    dict(repo="Food-Delivery-Web-App", metric="lighthouse performance",
         value="98/100", detail="Optimized React rendering, bundle splitting & Redux Toolkit memoization",
         env="Vercel · Chrome Desktop · 2026", source="lighthouse-report.json",
         bar=0.98),
    dict(repo="NHIT-Digital-Platform", metric="bank reconciliation",
         value="100% UTR", detail="Automated direct banking UTR reconciliation & statutory tax deduction",
         env="Production Banking Gateway", source="reports/reconciliation.md",
         bar=1.0),
    dict(repo="Youtube-Clone", metric="ui frame rate",
         value="60 FPS", detail="Hardware-accelerated CSS transforms and virtualization for infinite feeds",
         env="Chrome · React 18 · Client", source="benchmarks/fps.json",
         bar=0.95),
]

# ---------------------------------------------------------------------------
# Regulatory / Roadmap Deadlines
# ---------------------------------------------------------------------------
PQC_DEADLINES = [
    dict(date="2026-11-01", label="Platform Scaling",
         note="Scale NHIT digital platform microservices and distributed caching across regional clusters"),
    dict(date="2027-03-01", label="Cloud & Kubernetes",
         note="Automate multi-cloud GitOps pipelines with Helm, ArgoCD, and automated canary deployments"),
    dict(date="2027-09-01", label="Real-time Systems",
         note="Publish high-throughput Go distributed event streaming harnesses to open source"),
    dict(date="2029-01-01", label="Principal Architect",
         note="Lead enterprise digital transformations and mission-critical cloud platform engineering globally"),
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
    dict(key="2018", label="FOUNDATIONS", accent="cyan",
         note="B.Tech Computer Science begins — Core algorithms, data structures & systems programming"),
    dict(key="2020", label="FULL STACK", accent="blue",
         note="Building modern web applications with JavaScript, React, and backend APIs"),
    dict(key="2022", label="GRADUATION", accent="purple",
         note="Completing B.Tech CS capstones, distributed databases & cloud deployments"),
    dict(key="2024", label="PLATFORM DEV", accent="orange",
         note="Architecting high-scale platforms, microservices in Go, and financial automation"),
    dict(key="2026", label="SYSTEMS PRO", accent="red",
         note="Engineering enterprise-grade digital operating systems and resilient backend architecture"),
]

JOURNEY_MILES = [
    dict(date="2018-08", label="B.Tech CS Begins", sub="Computer Science Engineering", lane="down", accent="cyan"),
    dict(date="2020-03", label="Modern Web UIs", sub="React & Component Architecture", lane="up", accent="blue"),
    dict(date="2021-06", label="Full Stack Builds", sub="Node.js, Express & Databases", lane="up", accent="blue"),
    dict(date="2022-05", label="B.Tech CS Graduate", sub="Final Year Engineering Capstones", lane="down", accent="purple"),
    dict(date="2023-02", label="Go Microservices", sub="Concurrent backend development", lane="up", accent="purple"),
    dict(date="2024-01", label="Food Delivery App", sub="React, Redux Toolkit & Docker", lane="up", accent="orange"),
    dict(date="2024-08", label="Distributed Systems", sub="Caching, OTP store & rate limiting", lane="down", accent="orange"),
    dict(date="2025-03", label="NHIT Platform", sub="National infrastructure operating system", lane="up", accent="orange"),
    dict(date="2025-10", label="Banking Automation", sub="Direct UTR reconciliation & Sec 194C", lane="up", accent="red"),
    dict(date="2026-04", label="Enterprise Harness", sub="Architectural resilience & security", lane="up", accent="red"),
]

PUBLICATIONS = dict(
    counts=[("4+", "YEARS", "Engineering"),
            ("10+", "PROJECTS", "Systems & Full Stack"),
            ("99.9%", "UPTIME", "Mission Critical")],
    venues=[
        "Full Stack & Backend Systems Engineer",
        "Lead Architect on NHIT Digital Platform (National Highways Infra Trust)",
        "Core expertise: Go, React, TypeScript, Python, Microservices & Docker",
        "Specialized in Financial Automation, Banking UTR Reconciliation & Statutory Deductions"
    ],
)

IMPACT = [
    ("45ms", "P99 Latency", "High-throughput Go backend microservices & indexed relational storage"),
    ("100%", "Automated", "Section 194C statutory tax deductions and banking UTR reconciliation"),
    ("Zero", "Downtime", "Containerized deployment with automated recovery and health monitoring"),
    ("SSO & OTP", "Security", "Hardened OAuth 2.0 / Google SSO and distributed memory-safe OTP stores"),
]

EARLIER = []

CAREER_LINE = "Full Stack Engineer & Systems Architect · B.Tech CS · Specialized in Go, React & Scalable Cloud Platforms"
