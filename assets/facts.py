"""
Verified, hand-curated facts for Harshit Nain's profile dashboard & pipeline.
Directly reflecting Harshit's resume, credentials, and production engineering impact.
"""

OWNER = "HarshitNain"
NAME = "Harshit Nain"
TAGLINE = "Full Stack Developer | Golang | Node.js | React.js | Next.js | Microservices"
SUBLINE = "Architecting scalable Golang microservices, event-driven distributed pipelines, and responsive frontend systems."

# ---------------------------------------------------------------------------
# The flagship portfolio — reflecting Harshit's CV projects & production platforms
# ---------------------------------------------------------------------------
FLAGSHIPS = [
    # Backend & Distributed Systems
    dict(name="GRC-Distributed-Monolith", domain="Backend & APIs", lang="Go", tag="v2.1.0", private=False,
         blurb="Production distributed system with modular boundaries, gRPC/Protobuf inter-service messaging, NATS JetStream pub/sub, Kong API Gateway, and live React analytics."),
    dict(name="ARC-Automated-Rights-Consents", domain="Security & Compliance", lang="Go", tag="v1.4.0", private=False,
         blurb="End-to-end DPDP Act compliance microservice with 5+ consent workflows, embeddable JS widgets, audit-proof logging, Kafka, Redis, and HashiCorp Vault."),
    dict(name="Enterprise-SyncHub", domain="Backend & APIs", lang="Go", tag="v1.0.0", private=True,
         blurb="High-concurrency synchronization gateway, distributed event bus, and persistent agent communication harness in Golang."),

    # Full Stack & Production Engineering
    dict(name="NHIT-Digital-Platform", domain="Full Stack Development", lang="Go", tag="v1.2.0", private=False,
         blurb="Next-generation digital operating system for National Highways Infra Trust (NHIT). Automating green notes, Section 194C TDS, and direct banking reconciliation."),
    dict(name="AppSquadz-Core-APIs", domain="Backend & APIs", lang="JavaScript", tag="v1.0.0", private=True,
         blurb="15+ scalable RESTful API endpoints powering core workflows and partner integrations using Node.js, Express, and Redux Toolkit across 30+ responsive screens."),

    # Modern Frontend & Responsive Applications
    dict(name="Food-Villa", domain="Frontend & UI", lang="JavaScript", tag="v1.1.0", private=False,
         blurb="Interactive food ordering web application with dynamic restaurant filtering, real-time location tracking via Geolocation API, and Redux Toolkit cart persistence."),
    dict(name="Food-Delivery-Web-App", domain="Frontend & UI", lang="JavaScript", tag="v1.0.0", private=False,
         blurb="Full-featured food delivery app built with React.js, Redux Toolkit, Material UI (MUI), and Context API."),

    # Security & API Infrastructure
    dict(name="Secure-Gateway-Shield", domain="Security & Compliance", lang="Go", tag="v1.0.0", private=True,
         blurb="Kong API Gateway integration with JWT authentication, custom routing, and strict rate limiting protecting 20+ public endpoints."),
]

DOMAINS = [
    "Backend & APIs",
    "Full Stack Development",
    "Frontend & UI",
    "Security & Compliance",
]

# ---------------------------------------------------------------------------
# Verified production metrics directly from Harshit's resume & benchmarks
# ---------------------------------------------------------------------------
BENCHMARKS = [
    dict(repo="GRC-Distributed-Monolith", metric="event latency cut",
         value="-25%", detail="Kafka & NATS JetStream asynchronous messaging cutting inter-service latency",
         env="Golang gRPC · Kafka · 2026", source="benchmarks/latency.json",
         bar=0.75),
    dict(repo="React / Next.js Modules", metric="page load reduction",
         value="-30%", detail="TanStack Query server-state caching & optimized responsive component rendering",
         env="Next.js · React · Chrome Desktop", source="lighthouse-report.json",
         bar=0.88),
    dict(repo="Kong API Gateway", metric="protected endpoints",
         value="20+ APIs", detail="Configured JWT authentication, custom routing, and strict rate limiting",
         env="Kong API Gateway · Production", source="kong/gateway.yml",
         bar=0.95),
    dict(repo="Real-Time Telemetry", metric="active sessions",
         value="500+ Live", detail="High-concurrency WebSockets synchronizing live operational metrics seamlessly",
         env="Distributed WebSocket Cluster", source="telemetry/ws.go",
         bar=0.92),
]

# ---------------------------------------------------------------------------
# Engineering Roadmap Deadlines
# ---------------------------------------------------------------------------
PQC_DEADLINES = [
    dict(date="2026-11-01", label="Distributed Observability",
         note="Deploy OpenTelemetry, Jaeger distributed tracing, and Prometheus metrics across all Golang microservices"),
    dict(date="2027-03-01", label="Kubernetes & GitOps",
         note="Automate multi-region EKS deployments with ArgoCD, Helm charts, and canary release pipelines"),
    dict(date="2027-09-01", label="Open Source Streaming",
         note="Publish high-throughput Golang event streaming and NATS JetStream orchestration libraries to open source"),
    dict(date="2028-06-01", label="Principal Systems Architect",
         note="Lead enterprise digital transformations and mission-critical cloud platform engineering globally"),
]

# GitHub linguist colors
LANG_COLORS = {
    "Go": "#00ADD8", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "Python": "#3572A5", "HTML": "#e34c26", "CSS": "#563d7c",
    "C++": "#f34b7d", "Shell": "#89e051"
}

# ===========================================================================
# Professional Experience & Journey (Directly from CV)
# ===========================================================================

JOURNEY_ERAS = [
    dict(key="2019", label="ACADEMICS", accent="cyan",
         note="B.Tech Computer Science & Engineering begins — Core algorithms, data structures & systems programming"),
    dict(key="2021", label="WEB ENGINES", accent="blue",
         note="Modern web architecture — React.js, Next.js, Redux Toolkit, Node.js & RESTful APIs"),
    dict(key="2023", label="GRADUATION", accent="purple",
         note="Graduated B.Tech CSE (CGPA 7.4) — Scalable software engineering & cloud fundamentals"),
    dict(key="2024", label="APPSQUADZ", accent="orange",
         note="Full Stack Developer at AppSquadz — 15+ REST endpoints, React modules, Redux Toolkit state standardization"),
    dict(key="2025", label="RNR CONSULTING", accent="pink",
         note="Full Stack Developer at RNR — Golang microservices, gRPC, Protobuf, Kafka, NATS JetStream & Kong Gateway"),
    dict(key="2026", label="SYSTEMS ARCH", accent="green",
         note="Engineering DPDP compliance microservices, distributed monoliths & high-throughput real-time systems"),
]

JOURNEY_MILES = [
    dict(date="2019-08", label="B.Tech CSE Begins", sub="Anangpuria Institute of Tech & Mgmt", lane="down", accent="cyan"),
    dict(date="2021-04", label="Frontend Mastery", sub="React.js, Redux Toolkit & UI Modules", lane="up", accent="blue"),
    dict(date="2022-03", label="Full Stack Capstones", sub="Node.js, Express & PostgreSQL", lane="up", accent="blue"),
    dict(date="2023-06", label="B.Tech CSE Graduate", sub="Graduated with 7.4 CGPA in CSE", lane="down", accent="purple"),
    dict(date="2023-11", label="Go Microservices", sub="High-concurrency Golang & gRPC", lane="up", accent="purple"),
    dict(date="2024-01", label="AppSquadz Pvt. Ltd.", sub="Full Stack Dev · 15+ APIs & 30+ Screens", lane="up", accent="orange"),
    dict(date="2024-09", label="AWS Cloud Practitioner", sub="AWS Certified Cloud Practitioner", lane="down", accent="orange"),
    dict(date="2025-05", label="RNR Consulting", sub="Full Stack Dev · 5+ Go Microservices", lane="up", accent="pink"),
    dict(date="2025-08", label="Event-Driven Core", sub="Kafka & NATS JetStream (-25% Latency)", lane="up", accent="pink"),
    dict(date="2025-11", label="DPDP Act Compliance", sub="ARC Consent Engine & Audit Logging", lane="down", accent="red"),
    dict(date="2026-02", label="Kong Gateway & JWT", sub="Securing 20+ Public Endpoints", lane="up", accent="cyan"),
    dict(date="2026-04", label="Real-Time Telemetry", sub="WebSockets across 500+ Active Sessions", lane="up", accent="green"),
]

PUBLICATIONS = dict(
    counts=[("1.4+", "YEARS", "Production Experience"),
            ("5+", "SERVICES", "Golang, gRPC & Kafka"),
            ("500+", "ACTIVE", "Live WebSockets")],
    venues=[
        "Full Stack Developer at RNR Consulting Pvt. Ltd. (May 2025 – Present)",
        "Former Full Stack Developer at AppSquadz Pvt. Ltd. (Jan 2024 – Oct 2024)",
        "B.Tech Computer Science and Engineering (CGPA: 7.4) — AITM (2019–2023)",
        "Certifications: AWS Cloud Practitioner · DevOps Essentials · React Development",
        "Yukti Sangam Hackathon 2025 Participant at RNR Consulting Pvt. Ltd."
    ],
)

IMPACT = [
    ("-25% Latency", "Event-Driven", "Asynchronous workflows with Kafka and NATS JetStream cutting latency"),
    ("-30% Load Time", "TanStack Query", "Server-state caching across responsive React and Next.js frontend modules"),
    ("20+ Endpoints", "Kong Gateway", "Secured public endpoints with JWT authentication, custom routing & rate limiting"),
    ("DPDP Act", "Compliance ARC", "Automated Rights & Consents microservice with audit-proof data logging"),
]

EARLIER = []

CAREER_LINE = "Full Stack Developer · RNR Consulting Pvt. Ltd. · Specialized in Golang, gRPC, Kafka, React & Distributed Systems"
