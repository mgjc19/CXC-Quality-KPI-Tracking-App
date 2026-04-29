"""
Metrics and KPI definitions sourced from PSTG Quality metrics.xlsx.
Each project type maps to an ordered list of (stage_name, [metric_dicts]).

Last synced: 2026-04-29
"""

PROJECT_TYPES = [
    "Matured PDI",
    "Emerging PDI",
    "Brown Field Transformation",
    "Migration",
    "Upgrade",
]

# ── Matured PDI ──────────────────────────────────────────────────────────────

_MATURED_PDI = [
    ("Pre Engagement", [
        {
            "kpi": "Sales to Delivery Handover Index",
            "kpi_detail": (
                "Handover components:\n"
                "1. Proposed solution mapped to customer business requirements signed off by delivery\n"
                "2. Project timelines\n"
                "3. SOW & Efforts review\n"
                "4. Assumptions & dependencies signed off by delivery\n"
                "5. RACI\n"
                "6. Customer Stakeholder Map\n"
                "7. Account team stakeholder details"
            ),
            "metric": "Handover Complete index = (Number of handover components completed / total number of handover components) × 100 — SLA >=98%",
            "input_type": "percentage",
        },
    ]),
    ("Design", [
        {
            "kpi": "Available Reference Architecture Used for Proposed Solution",
            "kpi_detail": "Whether an available reference architecture was used for the proposed solution.",
            "metric": "Yes/No (No will reduce efficiency as will need more efforts being non-standard deliverable)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Workaround Coverage of Identified Limitations/Feature Gaps",
            "kpi_detail": "Coverage of workarounds for identified feature limitations/gaps.",
            "metric": "Workaround Coverage (%) = (Number of identified limitations with defined workaround / Total known limitations) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Digitized Delivery (as-a-code) Assessment Done",
            "kpi_detail": "Whether an assessment for digitized delivery (infrastructure/config as code) has been completed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Projected Automation Efficiency",
            "kpi_detail": "Projected efficiency gains from automation.",
            "metric": "Projected hours saving / total number of hours scoped",
            "input_type": "percentage",
        },
        {
            "kpi": "Adherence to Standard Design Templates",
            "kpi_detail": "Rate of adherence to standard design templates.",
            "metric": "(Number of deliverables using standard design templates / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Design Internal Peer Review Compliance Rate",
            "kpi_detail": (
                "Items in design peer review checklist:\n"
                "1. All customer requirements mapped in the design\n"
                "2. Limitations & Trade-offs clearly documented\n"
                "3. Integration/Third party dependencies addressed\n"
                "4. Security and Regulatory Compliance requirements covered\n"
                "5. Customer dependencies called out — Environment Readiness"
            ),
            "metric": "(Number of deliverables peer reviewed & approved / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right Design Approved (Internal)",
            "kpi_detail": "First-time approval rate for designs during internal review.",
            "metric": "(Number of designs approved in first review internal / Total designs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right Design Approved (Customer)",
            "kpi_detail": "First-time approval rate for designs by customer.",
            "metric": "(Number of designs approved in first review customer / Total designs submitted for review customer) × 100",
            "input_type": "percentage",
        },
    ]),
    ("Implementation Planning", [
        {
            "kpi": "Implementation Strategy Readiness",
            "kpi_detail": (
                "Components:\n"
                "1. Design sign off from customer\n"
                "2. Implementation sequence/runbook\n"
                "3. Lab Validation and BU validation for complex design\n"
                "4. Communication plan\n"
                "5. Dependency mapping\n"
                "6. Implementation readiness assessment\n"
                "7. Change management plan\n"
                "8. Test plan ready covering all customer approved use cases\n"
                "9. Integration dependencies with third party called out and addressed\n"
                "10. Rollback plan"
            ),
            "metric": "Implementation Plan Completeness (%) = (Number of completed implementation plan components / Total required components) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Agreement on T-Schedule",
            "kpi_detail": "Whether the T-Schedule has been agreed upon.",
            "metric": "Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
        {
            "kpi": "NIPs/MOPs Internal Reviewed",
            "kpi_detail": "NIPs/MOPs internally reviewed before sending to customer.",
            "metric": "(Number of deliverables peer reviewed / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right NIP/MOPs Approved (Internal)",
            "kpi_detail": "First-time approval rate of NIPs internally.",
            "metric": "(Number of NIPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (before approval)",
            "kpi_detail": "Average number of review cycles internally before NIP/MOP got approved.",
            "metric": "Average # of review cycles — Internal before it got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "1st Time Right NIP/MOPs Approved (External)",
            "kpi_detail": "First-time approval rate of NIPs by customer.",
            "metric": "(Number of NIPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — External (before approval)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before MOP got approved.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
    ]),
    ("Implementation & Testing", [
        {
            "kpi": "Documented CAB/Customer Approval Compliance Rate",
            "kpi_detail": "Compliance rate of documented CAB/customer approval prior to implementation window.",
            "metric": "(Number of Approved Changes / Total number of changes) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MW Success Rate as per Approved NIP/MOP",
            "kpi_detail": "Success rate of maintenance windows as per approved NIP/MOP.",
            "metric": "(Number of successful MWs / Total MWs) × 100% — SLA >=99%",
            "input_type": "percentage",
        },
        {
            "kpi": "NIP/MOP Failure Rate",
            "kpi_detail": "Deviations from NIP during implementation.",
            "metric": "(Number of successful MWs with NIP deviations / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Migration Windows Failure Rate (Cisco-Controlled)",
            "kpi_detail": "Failure rate attributable to Cisco-led execution or preparation gaps.",
            "metric": "(No. of MW unsuccessful due to Cisco-led execution or preparation gaps / Total MWs) × 100% — SLA <=1%",
            "input_type": "percentage",
        },
        {
            "kpi": "Rollback Success Rate",
            "kpi_detail": "Success rate of rollbacks when needed.",
            "metric": "(Number of Rollbacks successful / Total Rollbacks for a project) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Passing Rate of Test Cases",
            "kpi_detail": "Pass rate of executed test cases.",
            "metric": "(Number of test cases passed / Total number of test cases) × 100% — SLA 100%",
            "input_type": "percentage",
        },
    ]),
    ("Post Implementation", [
        {
            "kpi": "Knowledge Transfer",
            "kpi_detail": "Whether knowledge transfer to customer operations has been completed.",
            "metric": "Yes/No (No will be risk for customer operations)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Design Changes Documented & Customer Signoff",
            "kpi_detail": "Whether design changes are documented and customer signoff is secured.",
            "metric": "Yes/No (No will be risk for customer operations having incorrect or outdated design documentation)",
            "input_type": "yes_no",
        },
    ]),
    ("Overall Project", [
        {
            "kpi": "Escalations Count",
            "kpi_detail": "All escalations to follow with RCA.",
            "metric": "# Number of escalations reported",
            "input_type": "count",
        },
        {
            "kpi": "Risk & Lessons Learnt Register",
            "kpi_detail": "Whether a Risk & Lessons Learnt register is maintained.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSAT Score",
            "kpi_detail": "Customer Satisfaction score.",
            "metric": "CSAT",
            "input_type": "score",
        },
        {
            "kpi": "Adherence to Agreed T-Schedules",
            "kpi_detail": "Whether the project adhered to the agreed T-schedules.",
            "metric": "T-Schedule adherence = Yes/No (No is an impact to overall project, needs to be captured as lessons learnt)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Achieved Automation Efficiency",
            "kpi_detail": "Actual automation efficiency achieved during the project.",
            "metric": "Delivered Hours / Total hours scoped",
            "input_type": "percentage",
        },
    ]),
]

# ── Emerging PDI ─────────────────────────────────────────────────────────────

_EMERGING_PDI = [
    ("Pre Engagement", [
        {
            "kpi": "Feature Validation Score During POC Phase",
            "kpi_detail": "Applicable if CXC is part of POC/POVs. Feature Coverage >= 90%.",
            "metric": "Feature Coverage (%) = (Number of critical features validated (demo/lab/POC) / Total critical features identified) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Effort Estimate Validated and Agreed",
            "kpi_detail": "Whether the level of effort estimate has been validated and agreed.",
            "metric": "Yes — No Risk / No — Risk, requires LOE adjustment",
            "input_type": "yes_no",
        },
        {
            "kpi": "Sales to Delivery Handover Index",
            "kpi_detail": (
                "Handover components:\n"
                "1. Solution design proposal mapped to Project Business requirement\n"
                "2. Customer requirements mapped to project Milestones\n"
                "3. Assumptions & dependencies validated\n"
                "4. Customer Stakeholder contacts\n"
                "5. Project timelines aligned and agreed\n"
                "6. SOW covers the expected customer outcomes\n"
                "7. RACI\n"
                "8. Account team stakeholder details\n"
                "9. Sales to delivery handover meeting + MOM\n"
                "10. BU + TAC interlock details"
            ),
            "metric": "Handover Complete index = (Number of handover components received / total number of applicable components) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Requirement to Solution Gap Assessment Performed (Features)",
            "kpi_detail": "Whether a requirement-to-solution gap assessment has been performed for features.",
            "metric": "Yes/No (No is Risk)",
            "input_type": "yes_no",
        },
    ]),
    ("Design", [
        {
            "kpi": "Feature Limitations Addressable via Workaround",
            "kpi_detail": "Number of feature limitations that can be addressed using workarounds.",
            "metric": "# Number",
            "input_type": "count",
        },
        {
            "kpi": "BU Commitment to Address Feature Gaps Within Project Timelines",
            "kpi_detail": "Whether the BU has committed to addressing feature gaps within project timelines.",
            "metric": "Yes/No/Work In Progress",
            "input_type": "yes_no",
        },
        {
            "kpi": "Adherence to Customer Agreed Template",
            "kpi_detail": "Rate of adherence to customer agreed templates.",
            "metric": "(Number of deliverables using customer agreed template / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Design Internal Peer Review Compliance Rate",
            "kpi_detail": (
                "Items in design peer review checklist:\n"
                "1. All customer requirements mapped in the design\n"
                "2. Limitations & Trade-offs clearly documented\n"
                "3. Scale & Performance Validation from BU is performed\n"
                "4. Integration/Third party dependencies addressed\n"
                "5. Security and Regulatory Compliance requirements covered\n"
                "6. Customer dependencies called out — Environment Readiness"
            ),
            "metric": "(Number of deliverables peer reviewed & approved / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right Design Approved (Internal)",
            "kpi_detail": "First-time approval rate for designs during internal review.",
            "metric": "(Number of designs approved in first review internal / Total designs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right Design Approved (Customer)",
            "kpi_detail": "First-time approval rate for designs by customer.",
            "metric": "(Number of designs approved in first review customer / Total designs submitted for review customer) × 100",
            "input_type": "percentage",
        },
    ]),
    ("Implementation Planning", [
        {
            "kpi": "Implementation Strategy Readiness",
            "kpi_detail": (
                "Components:\n"
                "1. Design sign off from customer\n"
                "2. Implementation sequence/runbook\n"
                "3. Lab Validation and BU validation for complex design\n"
                "4. Communication plan\n"
                "5. Dependency mapping\n"
                "6. Environment readiness performed\n"
                "7. Change management plan\n"
                "8. Workaround of critical features\n"
                "9. Test plan ready covering all critical use cases\n"
                "10. Integration dependencies with third party called out and addressed\n"
                "11. Rollback plan"
            ),
            "metric": "Implementation Plan Completeness (%) = (Number of completed implementation plan components / Total required components) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Agreement on T-Schedule",
            "kpi_detail": "Whether the T-Schedule has been agreed upon.",
            "metric": "Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
        {
            "kpi": "NIPs Peer Reviewed",
            "kpi_detail": "NIPs internally reviewed before sending to customer.",
            "metric": "(Number of deliverables peer reviewed / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right NIP Approved (Internal)",
            "kpi_detail": "First-time approval rate of NIPs internally.",
            "metric": "(Number of NIPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (before approval)",
            "kpi_detail": "Average number of review cycles internally before NIP got approved.",
            "metric": "Average # of review cycles — Internal before it got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "1st Time Right NIP Approved (External)",
            "kpi_detail": "First-time approval rate of NIPs by customer.",
            "metric": "(Number of NIPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — External (before approval)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before MOP got approved.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
    ]),
    ("Implementation & Testing", [
        {
            "kpi": "Design Adherence Index",
            "kpi_detail": "Measures how closely implementation follows the approved design.",
            "metric": "(No. of features implemented as per design / Total critical features identified during POC) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Documented CAB/Customer Approval Compliance Rate",
            "kpi_detail": "Compliance rate of documented CAB/customer approval prior to implementation window.",
            "metric": "(Number of Approved Changes / Total number of changes) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MW Success Rate as per NIP",
            "kpi_detail": "Success rate of maintenance windows as per NIP.",
            "metric": "(Number of successful MWs / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "NIP Failure Rate",
            "kpi_detail": "Deviations from NIP during implementation.",
            "metric": "(Number of successful MWs with NIP deviations / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Passing Rate of Test Cases Post Implementation",
            "kpi_detail": "Post-implementation test case pass rate.",
            "metric": "(Number of test cases passed / Total number of test cases) × 100%",
            "input_type": "percentage",
        },
    ]),
    ("Post Implementation", [
        {
            "kpi": "Knowledge Transfer",
            "kpi_detail": "Whether knowledge transfer to customer operations has been completed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Design Changes Documented & Customer Signoff",
            "kpi_detail": "Whether design changes are documented and customer signoff is secured.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Day 2 Handover (LCS/CMS etc if Applicable)",
            "kpi_detail": "Whether Day 2 handover to LCS/CMS or equivalent team has been completed, if applicable.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
    ("Overall Project", [
        {
            "kpi": "Escalations Count",
            "kpi_detail": "All escalations to follow with RCA.",
            "metric": "# Number of escalations reported",
            "input_type": "count",
        },
        {
            "kpi": "Risk & Lessons Learnt Register",
            "kpi_detail": "Whether a Risk & Lessons Learnt register is maintained.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSAT Score",
            "kpi_detail": "Customer Satisfaction score.",
            "metric": "CSAT",
            "input_type": "score",
        },
        {
            "kpi": "Adherence to Agreed T-Schedules",
            "kpi_detail": "Whether the project adhered to the agreed T-schedules.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
]

# ── Brown Field Transformation ───────────────────────────────────────────────

_BF_TRANSFORMATION = [
    ("Pre Engagement", [
        {
            "kpi": "Sales to Delivery Handover Index",
            "kpi_detail": (
                "Handover components:\n"
                "1. Proposed solution mapped to customer business requirements signed off by delivery\n"
                "2. Project timelines\n"
                "3. SOW & Efforts review\n"
                "4. Assumptions & dependencies signed off by delivery\n"
                "5. RACI\n"
                "6. Customer Stakeholder Map\n"
                "7. Account team stakeholder details"
            ),
            "metric": "Handover Complete index = (Number of handover components completed / total number of handover components) × 100 — SLA >=98%",
            "input_type": "percentage",
        },
    ]),
    ("Design Approach Planning", [
        {
            "kpi": "Adherence to Customer Approved Templates & Lab-Validated MOPs",
            "kpi_detail": "Rate of adherence to standard customer approved templates and lab-validated MOPs.",
            "metric": "(Number of deliverables using Customer Approved Templates & Lab Validated / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Agreement on T-Schedule",
            "kpi_detail": "Whether the T-Schedule has been agreed upon.",
            "metric": "T-Schedule agreement = Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSA & FSA Customer Sign-off",
            "kpi_detail": (
                "CSA (Current State Architecture):\n"
                "Customer has reviewed, acknowledged, and signed off on the Current State Architecture (CSA) "
                "with confirmed understanding from all relevant stakeholders, ensuring no unresolved assumptions "
                "or open items remain — completed as per the baseline schedule.\n\n"
                "FSA (Future State Architecture):\n"
                "Customer has reviewed, acknowledged, and signed off on the Future State Architecture (FSA) "
                "with confirmed alignment across technical and business stakeholders, ensuring the proposed design "
                "is fully understood, agreed upon, and free of unresolved dependencies — completed as per the baseline schedule."
            ),
            "metric": "Yes — Positive, aligned to project timelines / No — Risk to project timelines",
            "input_type": "yes_no",
        },
        {
            "kpi": "FSA Design Approval Signed Off by Customer",
            "kpi_detail": "FSA Design Approval signed off by customer with documented exceptions/workarounds.",
            "metric": "Yes — Design limitations addressed and customer aligned / No — Risk during deployment & project timelines",
            "input_type": "yes_no",
        },
    ]),
    ("Implementation and Migration Plan", [
        {
            "kpi": "Implementation Strategy Readiness",
            "kpi_detail": (
                "Components:\n"
                "1. Design sign off from customer\n"
                "2. Implementation sequence/runbook\n"
                "3. Lab Validation and BU validation for complex design\n"
                "4. Communication plan\n"
                "5. Dependency mapping\n"
                "6. Implementation readiness assessment\n"
                "7. Change management plan\n"
                "8. Test plan ready covering all customer approved use cases\n"
                "9. Integration dependencies with third party called out and addressed\n"
                "10. Rollback plan\n"
                "11. Big Bang vs Phased migration Strategy discussed and agreed per site"
            ),
            "metric": "Implementation Plan Completeness (%) = (Number of completed implementation plan components / Total required components) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "MOP Internal Peer Review Compliance Rate",
            "kpi_detail": (
                "Items in MOP peer review checklist:\n"
                "1. Migration sequence and plan developed\n"
                "2. Rollback strategy\n"
                "3. Communication plan\n"
                "4. Dependency mapping\n"
                "5. Change management plan\n"
                "6. Environment readiness\n"
                "7. Test plan readiness\n"
                "8. Integration/Third party dependencies discussed and addressed"
            ),
            "metric": "(Number of deliverables/MOPs peer reviewed and approved internally / Total deliverables) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Pilot Testing and Validation Passed",
            "kpi_detail": "Whether pilot testing and validation has been completed and passed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Agreement on T-Schedule",
            "kpi_detail": "Whether the T-Schedule has been agreed upon.",
            "metric": "Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
        {
            "kpi": "NIPs Peer Reviewed",
            "kpi_detail": "NIPs peer reviewed before customer submission.",
            "metric": "(Number of deliverables peer reviewed / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right NIP (Greenfield) Approved Internal",
            "kpi_detail": "First-time approval rate for greenfield NIPs internally.",
            "metric": "(Number of NIPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (NIP)",
            "kpi_detail": "Average number of internal review cycles before NIP got approved.",
            "metric": "Average # of review cycles — Internal before it got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "1st Time Right NIP (Greenfield) Approved External",
            "kpi_detail": "First-time approval rate for greenfield NIPs by customer.",
            "metric": "(Number of NIPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — External (NIP)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before NIP got approved.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "1st Time Right MOP (Brownfield) Approved Internal",
            "kpi_detail": "First-time approval rate for brownfield MOPs internally.",
            "metric": "(Number of MOPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right MOP (Brownfield) Approved External",
            "kpi_detail": "First-time approval rate for brownfield MOPs by customer.",
            "metric": "(Number of MOPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (MOP)",
            "kpi_detail": "Average number of internal review cycles before MOP approval.",
            "metric": "Average # of review cycles — Internal before it got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "Avg Review Cycles — External (MOP)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before MOP approval.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
    ]),
    ("Implementation & Migration", [
        {
            "kpi": "Documented CAB/Customer Approval Compliance Rate",
            "kpi_detail": "Compliance rate of documented CAB/customer approval prior to migration.",
            "metric": "(Number of Approved Changes / Total number of changes) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MW Success Rate as per NIP",
            "kpi_detail": "Success rate of maintenance windows as per NIP.",
            "metric": "(Number of successful MWs / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "NIP (Greenfield) Failure Rate",
            "kpi_detail": "Deviations from NIP during implementation.",
            "metric": "(Number of successful MWs with NIP deviations / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MW Success Rate as per Approved MOP",
            "kpi_detail": "Success rate of maintenance windows as per approved MOP.",
            "metric": "(Number of successful MWs / Total MWs) × 100% — SLA >=99%",
            "input_type": "percentage",
        },
        {
            "kpi": "MOP (Brownfield) Failure Rate",
            "kpi_detail": "Failure rate due to incorrect MOP.",
            "metric": "(Number of successful MWs with MOP deviations / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Migration Windows Failure Rate (Cisco-Controlled)",
            "kpi_detail": "Failure rate attributable to Cisco-led execution or preparation gaps.",
            "metric": "(No. of MW unsuccessful due to Cisco-led execution or preparation gaps / Total MWs) × 100% — SLA <=1%",
            "input_type": "percentage",
        },
        {
            "kpi": "Rollback Success Rate",
            "kpi_detail": "Success rate of rollbacks when needed.",
            "metric": "(Number of Rollbacks successful / Total Rollbacks for a project) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Passing Rate of Test Cases",
            "kpi_detail": "Pass rate of executed test cases.",
            "metric": "(Number of test cases passed / Total number of test cases) × 100% — SLA 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Adherence to T-Schedule",
            "kpi_detail": "Whether the implementation adhered to the T-Schedule.",
            "metric": "Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
    ]),
    ("Post Implementation", [
        {
            "kpi": "Customer Signoff on Knowledge Transfer",
            "kpi_detail": "Whether knowledge transfer to customer has been completed and signed off.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Design Changes Documented & Customer Signoff",
            "kpi_detail": "Whether design changes are documented and customer signoff is secured.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
    ("Overall Project", [
        {
            "kpi": "Escalations Count",
            "kpi_detail": "All escalations to follow with RCA.",
            "metric": "# Number of escalations reported",
            "input_type": "count",
        },
        {
            "kpi": "Risk & Lessons Learnt Register",
            "kpi_detail": "Whether a Risk & Lessons Learnt register is maintained.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSAT Score",
            "kpi_detail": "Customer Satisfaction score.",
            "metric": "CSAT",
            "input_type": "score",
        },
    ]),
]

# ── Migration ────────────────────────────────────────────────────────────────

_MIGRATION = [
    ("Pre Engagement", [
        {
            "kpi": "Sales to Delivery Handover Index",
            "kpi_detail": (
                "Handover components:\n"
                "1. Proposed solution mapped to customer business requirements signed off by delivery\n"
                "2. Project timelines\n"
                "3. Assumptions & dependencies signed off by delivery\n"
                "4. Customer Stakeholder contacts\n"
                "5. SOW review\n"
                "6. RACI\n"
                "7. Account team stakeholder details"
            ),
            "metric": "Handover Complete index = (Number of handover components completed / total number of handover components) × 100 — SLA >=98%",
            "input_type": "percentage",
        },
    ]),
    ("Migration Approach Planning", [
        {
            "kpi": "Adherence to Customer Approved Templates & Lab-Validated MOPs",
            "kpi_detail": "Rate of adherence to standard customer approved templates and lab-validated MOPs.",
            "metric": "(Number of deliverables using Customer Approved Templates & Lab Validated / Total deliverables) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Agreement on T-Schedule",
            "kpi_detail": "Whether the T-Schedule has been agreed upon.",
            "metric": "T-Schedule agreement = Yes/No (No is a risk)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Digitized Delivery (as-a-code) Assessment Done",
            "kpi_detail": "Whether an assessment for digitized delivery (infrastructure/config as code) has been completed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Projected Automation Efficiency",
            "kpi_detail": "Projected efficiency gains from automation.",
            "metric": "Projected hours saving / total number of hours scoped",
            "input_type": "percentage",
        },
        {
            "kpi": "Like-for-Like Feature Parity Assessment",
            "kpi_detail": "Whether a like-for-like feature parity assessment has been performed (overall project success and early indicator).",
            "metric": "(Number of like-to-like features mapped / Total number of features deployed) × 100%",
            "input_type": "percentage",
        },
    ]),
    ("Migration Plan", [
        {
            "kpi": "MOP Internal Peer Review Compliance Rate",
            "kpi_detail": (
                "Items in MOP peer review checklist:\n"
                "1. Migration sequence and plan developed\n"
                "2. Rollback strategy\n"
                "3. Communication plan\n"
                "4. Dependency mapping\n"
                "5. Change management plan\n"
                "6. Environment readiness\n"
                "7. Test plan readiness\n"
                "8. Integration/Third party dependencies discussed and addressed"
            ),
            "metric": "(Number of deliverables/MOPs peer reviewed and approved internally / Total deliverables) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right MOP Approved (Internal)",
            "kpi_detail": "First-time approval rate for MOPs internally.",
            "metric": "(Number of MOPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right MOP Approved (External)",
            "kpi_detail": "First-time approval rate for MOPs by customer.",
            "metric": "(Number of MOPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (before MOP approval)",
            "kpi_detail": "Average number of internal review cycles before MOP got approved.",
            "metric": "Average # of review cycles — Internal before it got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "Avg Review Cycles — External (before MOP approval)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before MOP got approved.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
    ]),
    ("Migration & Testing", [
        {
            "kpi": "Documented CAB/Customer Approval Compliance Rate",
            "kpi_detail": "Compliance rate of documented CAB/customer approval prior to migration.",
            "metric": "(Number of Approved Changes / Total number of changes) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MW Success Rate as per Approved MOP",
            "kpi_detail": "Success rate of maintenance windows as per approved MOP.",
            "metric": "(Number of successful MWs / Total MWs) × 100% — SLA >=99%",
            "input_type": "percentage",
        },
        {
            "kpi": "MOP Failure Rate",
            "kpi_detail": "Failure rate due to MOP deviations.",
            "metric": "(Number of successful MWs with MOP deviations / Total MWs) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Migration Windows Failure Rate (Cisco-Controlled)",
            "kpi_detail": "Failure rate attributable to Cisco-led execution or preparation gaps.",
            "metric": "(No. of MW unsuccessful due to Cisco-led execution or preparation gaps / Total MWs) × 100% — SLA <=1%",
            "input_type": "percentage",
        },
        {
            "kpi": "Rollback Success Rate",
            "kpi_detail": "Success rate of rollbacks when needed.",
            "metric": "(Number of Rollbacks successful / Total Rollbacks for a project) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Passing Rate of Test Cases",
            "kpi_detail": "Pass rate of executed test cases.",
            "metric": "(Number of test cases passed / Total number of test cases) × 100% — SLA 100%",
            "input_type": "percentage",
        },
    ]),
    ("Overall Project", [
        {
            "kpi": "Escalations Count",
            "kpi_detail": "All escalations to follow with RCA.",
            "metric": "# Number of escalations reported",
            "input_type": "count",
        },
        {
            "kpi": "Risk & Lessons Learnt Register",
            "kpi_detail": "Whether a Risk & Lessons Learnt register is maintained.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSAT Score",
            "kpi_detail": "Customer Satisfaction score.",
            "metric": "CSAT",
            "input_type": "score",
        },
        {
            "kpi": "Adherence to Agreed T-Schedules",
            "kpi_detail": "Whether the project adhered to the agreed T-schedules.",
            "metric": "T-Schedule adherence = Yes/No (No is an impact to overall project, needs to be captured as lessons learnt)",
            "input_type": "yes_no",
        },
    ]),
]

# ── Upgrade ──────────────────────────────────────────────────────────────────

_UPGRADE = [
    ("Pre Engagement", [
        {
            "kpi": "Sales/Internal to Delivery Handover Index",
            "kpi_detail": (
                "Handover components:\n"
                "1. Customer requirements/reason for upgrade is captured\n"
                "2. Proposed Software version\n"
                "3. Customer Stakeholder contacts\n"
                "4. Project timelines aligned and agreed\n"
                "5. SOW — Scope and RACI review\n"
                "6. Account team stakeholder details\n"
                "7. Sales to delivery handover meeting + MOM"
            ),
            "metric": "Handover Complete index = (Number of handover components completed / total number of handover components) × 100 — SLA >=98%",
            "input_type": "percentage",
        },
        {
            "kpi": "Compatibility Check/Dependencies Reviewed",
            "kpi_detail": "Whether compatibility checks and dependencies have been reviewed and shared with customer.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Software & Hardware Compatibility/Interdependency",
            "kpi_detail": "Whether software and hardware compatibility and interdependency checks have been performed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "Integration/Third Party Dependencies",
            "kpi_detail": "Whether integration and third-party dependencies have been identified and addressed.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
    ("Upgrade Strategy", [
        {
            "kpi": "Bug Scrub Report Review — Account SME",
            "kpi_detail": "Whether the bug scrub report has been reviewed by the account SME.",
            "metric": "Yes/No (No is a risk as the report might miss customer relevant bugs)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Bug Scrub Report Review — With Customer",
            "kpi_detail": "Whether the bug scrub report has been reviewed with the customer.",
            "metric": "Yes/No (No is a risk as customer would not be aware of the potential risks associated)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Workaround Coverage of Applicable Critical Bugs",
            "kpi_detail": "Whether workarounds for applicable critical bugs have been identified.",
            "metric": "Yes/No (No is a risk as failing this would leave defects that can impact performance or availability)",
            "input_type": "yes_no",
        },
        {
            "kpi": "Upgrade Strategy Completeness Checklist",
            "kpi_detail": (
                "Checklist items:\n"
                "1. Upgrade sequence and plan developed\n"
                "2. Rollback strategy (Backup and Restore)\n"
                "3. Communication plan\n"
                "4. Dependency mapping\n"
                "5. Change management plan\n"
                "6. Environment readiness\n"
                "7. Test plan readiness\n"
                "8. Pre checks and Post Checks\n"
                "9. Integration/Third party dependencies (pre-requisites called out)"
            ),
            "metric": "(Number of deliverables/Checklist peer reviewed and approved internally / Total deliverables) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Upgrade MOP Template",
            "kpi_detail": "Whether the Upgrade MOP template has been peer reviewed and approved.",
            "metric": "(Number of deliverables/MOP peer reviewed and approved internally / Total deliverables) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Lab Validation (Production/Test Lab)",
            "kpi_detail": "Whether lab validation has been performed.",
            "metric": "Yes/No (No is a risk as it can lead to catastrophic issues during or post upgrade)",
            "input_type": "yes_no",
        },
        {
            "kpi": "1st Time Right MOP Approved (Internal)",
            "kpi_detail": "First-time approval rate for MOPs internally.",
            "metric": "(Number of MOPs approved in first review internal / Total MOPs submitted for review internal) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "1st Time Right MOP Approved (External)",
            "kpi_detail": "First-time approval rate for MOPs by customer.",
            "metric": "(Number of MOPs approved in first review customer / Total MOPs submitted for review customer) × 100",
            "input_type": "percentage",
        },
        {
            "kpi": "Avg Review Cycles — Internal (before MOP approval)",
            "kpi_detail": "Average number of internal review cycles before MOP got approved.",
            "metric": "Average # of review cycles — Internal before MOP got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "Avg Review Cycles — External (before MOP approval)",
            "kpi_detail": "Average number of review cycles with customer Tech Review Board before MOP got approved.",
            "metric": "Average # of review cycles — external before MOP got approved <=2",
            "input_type": "number",
        },
        {
            "kpi": "Proactive TAC/BU Alignment",
            "kpi_detail": "Whether proactive alignment with TAC/BU has been established.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
    ("Upgrade Execution", [
        {
            "kpi": "Upgrade MOP Document Creation (Site/Device Specific)",
            "kpi_detail": (
                "Site/device-specific MOP including:\n"
                "1. Rollback strategy (Backup and Restore)\n"
                "2. Communication plan\n"
                "3. Environment readiness\n"
                "4. Test plan readiness\n"
                "5. Pre checks and Post Checks\n"
                "6. Integration/Third party dependencies (pre-requisites called out)"
            ),
            "metric": "(Number of deliverables/MOP peer reviewed and approved internally / Total deliverables) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Upgrade Pre-check Validation",
            "kpi_detail": "Validation of pre-checks as per MOP.",
            "metric": "(Number of successful pre checks / Total number of pre checks) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Documented CAB/Customer Approval Compliance Rate",
            "kpi_detail": "Compliance rate of documented CAB/customer approval prior to upgrades.",
            "metric": "(Number of Approved Changes / Total number of changes) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Upgrade Success Rate as per Approved MOP",
            "kpi_detail": "Success rate of upgrades as per approved MOP.",
            "metric": "(Number of successful Upgrades / Total Upgrades) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "MOP Failure Rate",
            "kpi_detail": "Rate of upgrades with MOP deviations.",
            "metric": "(Number of successful upgrades with MOP deviations / Total upgrades) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Rollback Success Rate",
            "kpi_detail": "Success rate of rollbacks when needed.",
            "metric": "(Number of Rollbacks successful / Total Rollbacks for a project) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Passing Rate of Test Cases",
            "kpi_detail": "Pass rate of executed test cases.",
            "metric": "(Number of test cases passed / Total number of test cases) × 100% — SLA 100%",
            "input_type": "percentage",
        },
    ]),
    ("Post Upgrade", [
        {
            "kpi": "Upgrade Post-check Validation",
            "kpi_detail": "Validation of post-checks as per MOP.",
            "metric": "(Number of successful post checks / Total number of post checks) × 100% — SLA =100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Knowledge Transfer (If Added Feature Set)",
            "kpi_detail": "Knowledge transfer in case of added feature set.",
            "metric": "Yes/No (No is a risk for adoption of any added/new feature, if an objective of the upgrade)",
            "input_type": "yes_no",
        },
    ]),
    ("Overall Project", [
        {
            "kpi": "Escalations Count",
            "kpi_detail": "All escalations to follow with RCA.",
            "metric": "# Number of escalations reported",
            "input_type": "count",
        },
        {
            "kpi": "Risk & Lessons Learnt Register",
            "kpi_detail": "Whether a Risk & Lessons Learnt register is maintained.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
        {
            "kpi": "CSAT Score",
            "kpi_detail": "Customer Satisfaction score.",
            "metric": "CSAT",
            "input_type": "score",
        },
        {
            "kpi": "Upgrade Failure Rate (Cisco-Controlled)",
            "kpi_detail": "Failure rate attributable to Cisco-led execution or preparation gaps.",
            "metric": "(No. of unsuccessful upgrades due to Cisco-led execution or preparation gaps / Total number of Upgrades) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Adherence to Agreed T-Schedules",
            "kpi_detail": "Whether the project adhered to the agreed T-schedules.",
            "metric": "T-Schedule adherence = Yes/No (No is an impact to overall project, needs to be captured as lessons learnt)",
            "input_type": "yes_no",
        },
    ]),
]


# ── Master lookup ────────────────────────────────────────────────────────────

PROJECT_TYPE_CONFIG = {
    "Matured PDI": _MATURED_PDI,
    "Emerging PDI": _EMERGING_PDI,
    "Brown Field Transformation": _BF_TRANSFORMATION,
    "Migration": _MIGRATION,
    "Upgrade": _UPGRADE,
}


def get_stages(project_type):
    """Return ordered list of stage names for a project type."""
    return [s[0] for s in PROJECT_TYPE_CONFIG.get(project_type, [])]


def get_stage_metrics(project_type, stage):
    """Return list of metric dicts for a given project type and stage."""
    for s_name, metrics in PROJECT_TYPE_CONFIG.get(project_type, []):
        if s_name == stage:
            return metrics
    return []
