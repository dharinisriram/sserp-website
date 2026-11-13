export const site = {
  name: "SS ERP Solutions",
  email: "support@sserpsolutions.net",
  tagline: "Enterprise technology consulting, rooted in India, serving clients worldwide.",
};

export type Service = { slug: string; title: string; summary: string };

export const services: Service[] = [
  { slug: "erp-consulting", title: "ERP Consulting & Health Checks", summary: "Independent advice, health checks and optimisation roadmaps based on how your system actually performs." },
  { slug: "oracle-multi-erp", title: "Oracle & Multi-ERP Solutions", summary: "Consistent ERP support across Oracle, NetSuite and mixed enterprise landscapes." },
  { slug: "implementation", title: "Application Implementation", summary: "Enterprise application rollouts built on clear requirements, controlled delivery and real business needs." },
  { slug: "pmo", title: "PMO", summary: "Governance, coordination and delivery discipline for complex ERP programmes." },
  { slug: "analytics", title: "Analytics & Custom Dashboards", summary: "Turning ERP data into dashboards and insights that support faster decisions." },
  { slug: "training", title: "Training & Internships", summary: "Practical ERP skills through training, internships, mentoring and project exposure." },
  { slug: "greenfield-brownfield", title: "Greenfield & Brownfield", summary: "Choosing — and delivering — between building new systems or evolving the ones you have." },
  { slug: "ams", title: "Application Management Services", summary: "Ongoing SAP support that keeps live systems stable and performing." },
  { slug: "production-support", title: "Production Support & Enhancements", summary: "Steady SAP support and continuous improvements aligned with business needs." },
  { slug: "rollouts-upgrades", title: "Rollouts, Upgrades & Migrations", summary: "Upgrades, migrations and global rollouts that don't disrupt operations." },
  { slug: "digital-transformation", title: "Digital Transformation", summary: "Modernising core business systems without halting daily operations." },
  { slug: "ai-automation", title: "AI Integration & Intelligent Automation", summary: "Practical AI and automation for ERP processes, with attention to data, controls and governance." },
];

export const footerServices = ["ams", "production-support", "rollouts-upgrades", "erp-consulting"];

export const stages = [
  { n: "01", title: "Assess", text: "Understand the business, the ERP landscape and the priorities before choosing an approach." },
  { n: "02", title: "Plan", text: "Build a roadmap with priorities, timelines and outcomes tied to business goals." },
  { n: "03", title: "Deliver", text: "Implement with structured execution, expert guidance and minimal disruption." },
  { n: "04", title: "Improve", text: "Keep improving performance through ongoing support and continuous optimisation." },
];

export const caseStudies = [
  { title: "S/4HANA Transformation", stat: "9 months", text: "ECC to S/4HANA for a manufacturing group in India — without missing a single close." },
  { title: "Global SAP Rollout", stat: "4 countries", text: "One SAP template rolled out across four countries for an enterprise group." },
  { title: "SAP Application Management", stat: "24/7", text: "Ongoing ERP support and continuity for an enterprise client." },
];

export const engagementModels = [
  { title: "ERP Health Check", duration: "2–3 weeks", text: "A focused review that identifies key issues, risks and improvement opportunities." },
  { title: "Full ERP Engagement", duration: "Project-based", text: "End-to-end consulting for implementation, transformation, migration or optimisation." },
  { title: "Managed ERP Support", duration: "Ongoing", text: "Continuous application support, enhancements and optimisation." },
];
