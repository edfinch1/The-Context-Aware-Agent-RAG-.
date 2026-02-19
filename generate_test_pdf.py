"""
Generate a complex, realistic test PDF for RAG testing.
Acme Corp Employee Policy Manual - ~20 pages of dense policy with
buried details, contradictions, and specific numbers perfect for RAG demos.
"""
from fpdf import FPDF
import datetime

class PolicyPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "ACME CORP - EMPLOYEE POLICY & BENEFITS MANUAL - CONFIDENTIAL", align="C")
        self.ln(2)
        self.set_draw_color(180, 180, 180)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()} | Effective: 1 January 2025 | Version 7.4", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(20, 60, 120)
        self.ln(6)
        self.cell(0, 8, title, ln=True)
        self.set_draw_color(20, 60, 120)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def subsection(self, title):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self.ln(3)
        self.cell(0, 6, title, ln=True)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def clause(self, number, text):
        self.set_font("Helvetica", "B", 10)
        self.cell(18, 5.5, f"§{number}", ln=False)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

pdf = PolicyPDF()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

# --- COVER PAGE ---
pdf.set_font("Helvetica", "B", 26)
pdf.set_text_color(20, 60, 120)
pdf.ln(30)
pdf.cell(0, 15, "ACME CORP", align="C", ln=True)
pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 10, "Employee Policy & Benefits Manual", align="C", ln=True)
pdf.set_font("Helvetica", "", 12)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 8, "Version 7.4 | Effective 1 January 2025", align="C", ln=True)
pdf.cell(0, 8, "Issued by: People & Culture Division", align="C", ln=True)
pdf.ln(10)
pdf.set_font("Helvetica", "I", 10)
pdf.multi_cell(0, 6, "This document contains confidential and proprietary information. "
    "It supersedes all previous versions. All employees are required to read and acknowledge "
    "receipt within 14 days of commencement or upon any revision.", align="C")

# --- TABLE OF CONTENTS ---
pdf.add_page()
pdf.set_text_color(0, 0, 0)
pdf.section_title("Table of Contents")
toc = [
    ("Section 1", "Employment Classification & Probation", 3),
    ("Section 2", "Remuneration & Salary Review", 4),
    ("Section 3", "Annual & Personal Leave", 5),
    ("Section 4", "Parental & Carer's Leave", 7),
    ("Section 5", "Flexible Working Arrangements", 8),
    ("Section 6", "Expense Reimbursement Policy", 9),
    ("Section 7", "Code of Conduct & Disciplinary", 11),
    ("Section 8", "Information Security & Data", 13),
    ("Section 9", "Health, Safety & Wellbeing", 14),
    ("Section 10", "Termination & Redundancy", 16),
    ("Appendix A", "Benefit Entitlements by Level", 18),
    ("Appendix B", "Approved Vendors & Travel Policy", 19),
]
pdf.set_font("Helvetica", "", 10)
for section, title, page in toc:
    pdf.cell(35, 7, section, ln=False)
    pdf.cell(130, 7, title, ln=False)
    pdf.cell(0, 7, str(page), ln=True, align="R")

# --- SECTION 1: EMPLOYMENT ---
pdf.add_page()
pdf.section_title("Section 1: Employment Classification & Probation")
pdf.subsection("1.1 Employment Types")
pdf.body("Acme Corp recognises four employment classifications: Full-Time Permanent, Part-Time Permanent, "
    "Fixed-Term Contract, and Casual. Each classification carries different entitlements as detailed "
    "throughout this manual. Employees must confirm in writing their classification upon commencement.")

pdf.subsection("1.2 Probationary Period")
pdf.clause("1.2.1", "All new Full-Time and Part-Time employees are subject to a probationary period of "
    "six (6) months commencing from their start date.")
pdf.clause("1.2.2", "Fixed-Term employees engaged for periods of less than 12 months are subject to a "
    "probationary period of three (3) months.")
pdf.clause("1.2.3", "During probation, either party may terminate the employment agreement with a minimum "
    "notice of five (5) business days. Performance reviews are conducted at weeks 6, 12, and 24.")
pdf.clause("1.2.4", "Probation may be extended by up to a further 3 months at the sole discretion of "
    "the employee's direct manager, with written approval from the People & Culture Division.")

pdf.subsection("1.3 Salary Classification Levels")
pdf.body("Acme Corp operates a six-tier classification system (L1-L6). Employees are assigned a level "
    "at commencement based on skills, experience, and market benchmarking. Reclassification is reviewed "
    "annually but may occur off-cycle with written justification from a Director-level manager.")
pdf.body("Note: Employees at L1-L3 are classified as 'Individual Contributors'. Employees at L4-L5 are "
    "'Senior Contributors or Lead'. Employees at L6 are 'Director and above'. This distinction affects "
    "expense limits, travel class entitlements, and bonus structures (see Appendix A).")

# --- SECTION 2: REMUNERATION ---
pdf.add_page()
pdf.section_title("Section 2: Remuneration & Salary Review")
pdf.subsection("2.1 Pay Cycle")
pdf.body("All employees are paid fortnightly, with pay periods ending on the Sunday of alternating weeks. "
    "Payments are processed by 11:59 PM AEST on the Thursday following each pay period end date.")

pdf.subsection("2.2 Annual Salary Review (ASR)")
pdf.clause("2.2.1", "The Annual Salary Review window opens on 1 March each year and outcomes are effective "
    "from 1 April. Employees must have been employed for a minimum of six (6) months prior to 1 March "
    "to be eligible for an ASR adjustment in that cycle.")
pdf.clause("2.2.2", "The maximum base salary increase under an ASR is capped at 8% for L1-L4 employees "
    "and 12% for L5-L6, except in cases of reclassification.")
pdf.clause("2.2.3", "Employees who received an off-cycle salary adjustment of 5% or more in the preceding "
    "12-month period are ineligible for an ASR increase in the same calendar year.")
pdf.clause("2.2.4", "The company-wide ASR budget is determined each January by the Board and communicated "
    "to managers by the last business day of February.")

pdf.subsection("2.3 Performance Bonus")
pdf.body("Acme Corp operates a discretionary annual performance bonus scheme. Bonus eligibility and "
    "targets are outlined below:")
bonuses = [
    ("L1-L2", "0-5% of base salary", "90%+ of OKR targets"),
    ("L3-L4", "0-10% of base salary", "85%+ of OKR targets"),
    ("L5", "0-20% of base salary", "80%+ of OKR targets"),
    ("L6+", "0-30% of base salary + LTIP", "As per individual agreement"),
]
pdf.set_font("Helvetica", "B", 9)
pdf.cell(30, 7, "Level", border=1)
pdf.cell(70, 7, "Maximum Bonus", border=1)
pdf.cell(0, 7, "Eligibility Threshold", border=1, ln=True)
pdf.set_font("Helvetica", "", 9)
for level, bonus, threshold in bonuses:
    pdf.cell(30, 7, level, border=1)
    pdf.cell(70, 7, bonus, border=1)
    pdf.cell(0, 7, threshold, border=1, ln=True)
pdf.ln(4)
pdf.body("Bonuses are paid in the first pay cycle of July following the review period. Employees who "
    "resign before 30 June forfeit all bonus entitlements for that year, regardless of OKR performance.")

# --- SECTION 3: LEAVE ---
pdf.add_page()
pdf.section_title("Section 3: Annual Leave & Personal Leave")
pdf.subsection("3.1 Annual Leave Entitlement")
pdf.clause("3.1.1", "Full-Time employees accrue 20 days (4 weeks) of paid annual leave per year, "
    "accrued progressively at 1.6667 days per month.")
pdf.clause("3.1.2", "Employees in roles designated as 'Shift Work' receive an additional 5 days per year "
    "(25 days total). The list of shift-designated roles is maintained by People & Culture and "
    "reviewed in February of each year.")
pdf.clause("3.1.3", "Annual leave may be taken in advance with written manager approval. The maximum "
    "advance is 10 days. If employment is terminated while in advance, the shortfall is deducted "
    "from the final pay.")
pdf.clause("3.1.4", "Accrued leave is capped at 40 days (8 weeks). Once this cap is reached, no further "
    "leave accrues until the balance is reduced. Managers are responsible for proactively managing "
    "their team's leave balance.")
pdf.clause("3.1.5", "Annual leave loading of 17.5% applies to all roles at L1-L4. Employees at L5 and "
    "above are not entitled to leave loading as this is factored into their total remuneration package.")

pdf.subsection("3.2 Leave Requests & Blackout Periods")
pdf.body("All leave requests must be submitted via the HR portal no less than 10 business days in advance "
    "for leave of 5 days or fewer. For leave exceeding 5 consecutive days, 21 calendar days' notice "
    "is required. Emergency situations are assessed on a case-by-case basis.")
pdf.body("Blackout periods, during which annual leave requests will not generally be approved, are declared "
    "by the relevant Business Unit Head. Standard company-wide blackout periods are: the last two "
    "weeks of each financial year quarter (i.e., end of March, June, September, December) and the two "
    "weeks immediately preceding a major product launch, as defined by the CEO's office.")

pdf.subsection("3.3 Personal / Carer's Leave")
pdf.clause("3.3.1", "All permanent employees receive 10 days of paid personal leave (sick leave) per year, "
    "accrued at 0.8333 days per month. Casual employees are not entitled to personal leave.")
pdf.clause("3.3.2", "Personal leave may be used for personal illness, injury, or to care for an immediate "
    "family member. Immediate family is defined as: spouse or de facto partner, child, parent, sibling, "
    "grandparent, or grandchild.")
pdf.clause("3.3.3", "For personal leave exceeding two (2) consecutive days, a medical certificate or "
    "statutory declaration must be provided. Acme Corp reserves the right to request documentation "
    "for any absence at its discretion.")
pdf.clause("3.3.4", "Unused personal leave accrues indefinitely but does not attract leave loading and "
    "is not paid out upon termination of employment.")

pdf.subsection("3.4 Long Service Leave")
pdf.body("Employees who have completed 7 years of continuous service are entitled to long service leave "
    "(LSL) as per State/Territory legislation. For employees based in New South Wales: 2 months' leave "
    "is available after 10 years, with a pro-rata entitlement after 5 years in cases of genuine "
    "redundancy, death, or domestic pressing necessity. For Victoria-based employees: 6.067 weeks "
    "is payable after 7 years of service.")

# --- SECTION 4: PARENTAL LEAVE ---
pdf.add_page()
pdf.section_title("Section 4: Parental & Carer's Leave")
pdf.subsection("4.1 Primary Carer Leave")
pdf.clause("4.1.1", "Permanent employees who are the primary carer of a newborn or newly adopted child "
    "are entitled to 20 weeks of paid parental leave at their ordinary rate of pay, provided they "
    "have completed at least 12 months of continuous service prior to the expected date of birth "
    "or adoption placement.")
pdf.clause("4.1.2", "An additional 4 weeks of unpaid leave may be taken immediately following the "
    "paid period, for a total of 24 weeks leave. The employee must provide at least 10 weeks' "
    "notice of their intended leave commencement date.")
pdf.clause("4.1.3", "Employees who are currently on a Performance Improvement Plan (PIP) at the time "
    "of their leave request remain entitled to parental leave. However, the PIP is paused during "
    "the leave period and recommences upon return.")

pdf.subsection("4.2 Secondary Carer leave")
pdf.clause("4.2.1", "Permanent employees who are the secondary carer receive 4 weeks of paid secondary "
    "carer leave. This leave must be taken within 12 months of the child's birth or placement.")
pdf.clause("4.2.2", "Secondary carer leave can be taken in a single continuous block or split into "
    "two periods of at least 2 weeks each.")

pdf.subsection("4.3 Return to Work & Keeping in Touch")
pdf.body("Employees on parental leave may work up to 10 'Keeping in Touch' (KIT) days without it "
    "affecting their leave entitlement. KIT days must be agreed between the employee and manager "
    "and cannot be compelled by either party. Each KIT day is paid at the employee's ordinary daily rate.")

# --- SECTION 5: FLEXIBLE WORKING ---
pdf.add_page()
pdf.section_title("Section 5: Flexible Working Arrangements")
pdf.subsection("5.1 Work From Home Policy")
pdf.clause("5.1.1", "Acme Corp operates a hybrid work model. Employees are expected to be in the office "
    "a minimum of three (3) days per week. The specific days are agreed between the employee and "
    "their manager but Tuesday and Wednesday are designated as 'anchor days' for all teams, "
    "meaning attendance is mandatory unless travelling for business or on approved leave.")
pdf.clause("5.1.2", "Employees at L1 or in their first 6 months of employment may be required by their "
    "manager to attend the office up to five (5) days per week for mentoring and onboarding purposes.")
pdf.clause("5.1.3", "Work from home equipment: Acme Corp will provide a one-time home office allowance "
    "of $800 AUD for Full-Time permanent employees and $400 AUD for Part-Time permanent employees "
    "upon commencement, subject to manager approval. This allowance covers desk, chair, and monitor. "
    "Receipts must be submitted within 90 days.")

pdf.subsection("5.2 Formal Flexible Working Requests")
pdf.body("Eligible employees (those with at least 12 months of continuous service, or who are a parent "
    "or carer) may request a formal flexible working arrangement under the Flexible Work Act provisions. "
    "Requests must be submitted in writing to People & Culture. The company must respond within 21 days "
    "with either an approval, a counter-proposal, or a written refusal including business grounds.")

# --- SECTION 6: EXPENSES ---
pdf.add_page()
pdf.section_title("Section 6: Expense Reimbursement Policy")
pdf.subsection("6.1 Approval Thresholds")
pdf.body("All business expenses must have prior written approval except for those below the auto-approval "
    "threshold. Approval thresholds are based on the employee's level:")

expenses = [
    ("L1-L2", "$50", "$500", "Manager"),
    ("L3-L4", "$150", "$2,000", "Manager"),
    ("L5", "$500", "$5,000", "Director"),
    ("L6+", "$1,000", "Unlimited", "CFO or delegate"),
]
pdf.set_font("Helvetica", "B", 9)
pdf.cell(25, 7, "Level", border=1)
pdf.cell(40, 7, "Auto-Approve Limit", border=1)
pdf.cell(45, 7, "Single Claim Limit", border=1)
pdf.cell(0, 7, "Approver", border=1, ln=True)
pdf.set_font("Helvetica", "", 9)
for level, auto, limit, approver in expenses:
    pdf.cell(25, 7, level, border=1)
    pdf.cell(40, 7, auto, border=1)
    pdf.cell(45, 7, limit, border=1)
    pdf.cell(0, 7, approver, border=1, ln=True)
pdf.ln(4)

pdf.subsection("6.2 Meals & Entertainment")
pdf.clause("6.2.1", "Client meals and entertainment: up to $120 per person per occasion for L1-L4. "
    "Up to $250 per person for L5 and above. A guest list and business purpose must be documented.")
pdf.clause("6.2.2", "Team meals (internal only, no clients): Up to $45 per person. Maximum frequency "
    "of once per month per team. Must be approved by a Director or above.")
pdf.clause("6.2.3", "Working lunches delivered to the office are permitted at up to $25 per person "
    "when a meeting exceeds 3 hours and spans the lunch period (12:00-14:00).")

pdf.subsection("6.3 Travel")
pdf.clause("6.3.1", "Domestic economy class flights are standard for all employees. Business class "
    "is permitted for flights exceeding 4 hours in duration for L5 and above, and for any employee "
    "where a medical certificate supports the upgrade.")
pdf.clause("6.3.2", "International business class is permitted for L6 and above for all flights, and "
    "for L4-L5 for flights exceeding 8 hours, subject to CFO approval.")
pdf.clause("6.3.3", "Hotel accommodation is reimbursed at up to $250 per night in capital cities "
    "and $180 per night in regional locations. Exceptions require Director approval.")
pdf.clause("6.3.4", "A daily meal allowance ('per diem') of $85 applies when travelling for business "
    "more than 50km from the employee's primary office location, for each 24-hour period away.")

# --- SECTION 7: CODE OF CONDUCT ---
pdf.add_page()
pdf.section_title("Section 7: Code of Conduct & Disciplinary Procedure")
pdf.subsection("7.1 Expected Standards")
pdf.body("All Acme Corp employees, contractors, and representatives are held to the following standards: "
    "integrity in all dealings, respect for colleagues and stakeholders, compliance with all applicable "
    "laws and company policies, protection of confidential information, and avoidance of conflicts of interest.")
pdf.body("Any breach of the Code of Conduct may result in disciplinary action up to and including termination "
    "of employment. The severity of the response will be proportional to the nature, frequency, and "
    "impact of the breach, as assessed by People & Culture in consultation with the relevant manager.")

pdf.subsection("7.2 Conflicts of Interest")
pdf.clause("7.2.1", "Employees must declare any actual or potential conflict of interest to their manager "
    "and People & Culture within 5 business days of becoming aware of it. A register of declared "
    "conflicts is maintained by the Legal & Compliance team.")
pdf.clause("7.2.2", "Employees may not hold a shareholding of greater than 1% in a direct competitor "
    "or supplier of Acme Corp without written approval from the CEO.")
pdf.clause("7.2.3", "Employees must not accept gifts, hospitality, or other benefits from external "
    "parties valued above $150 AUD without prior written approval. Values between $50-$150 must "
    "be declared. All accepted gifts must be registered in the Gift Register within 3 business days.")

pdf.subsection("7.3 Disciplinary Process")
pdf.body("The standard disciplinary process follows these steps: (1) Manager discussion and verbal "
    "warning (documented), (2) Formal written warning issued by People & Culture, (3) Final written "
    "warning or Performance Improvement Plan (PIP), (4) Termination of employment. Steps may be "
    "skipped for serious misconduct, which includes but is not limited to: theft, fraud, harassment, "
    "and material breach of information security policies.")

# --- SECTION 8: INFORMATION SECURITY ---
pdf.add_page()
pdf.section_title("Section 8: Information Security & Data Handling")
pdf.subsection("8.1 Acceptable Use")
pdf.body("Acme Corp systems, devices, and networks are to be used for legitimate business purposes. "
    "Incidental personal use is tolerated provided it does not: interfere with work performance, "
    "involve access to illegal or inappropriate content, constitute a security risk, or involve "
    "use of company storage for personal media files exceeding 2GB.")

pdf.subsection("8.2 Password & Access Controls")
pdf.clause("8.2.1", "All corporate passwords must be at least 14 characters and include uppercase, "
    "lowercase, numbers, and symbols. Passwords must be rotated every 90 days.")
pdf.clause("8.2.2", "Multi-factor authentication (MFA) is mandatory for all corporate systems. "
    "Failure to enrol in MFA within 5 days of account creation will result in access suspension.")
pdf.clause("8.2.3", "Employees must not share access credentials under any circumstances. Shared "
    "service accounts require a formal request to IT Security with a documented business justification.")

pdf.subsection("8.3 Data Classification")
pdf.body("Acme Corp data is classified into four tiers: Public, Internal, Confidential, and Restricted. "
    "Customer PII, financial data, and board materials are Restricted. Employee HR and salary data "
    "is Confidential. Internal operational documents are Internal. All other published content is Public. "
    "Restricted data may only be stored on approved encrypted corporate devices and may not be "
    "transmitted via personal email or unapproved cloud services.")

# --- SECTION 9: H&S ---
pdf.add_page()
pdf.section_title("Section 9: Health, Safety & Wellbeing")
pdf.subsection("9.1 EAP - Employee Assistance Programme")
pdf.body("Acme Corp provides all permanent and fixed-term employees with access to the Acme EAP, "
    "delivered by LifeAssist Partners Pty Ltd. The programme offers up to 8 confidential counselling "
    "sessions per employee per calendar year, at no cost. Sessions may be for personal or work-related "
    "matters. The EAP is also available to an employee's immediate household members.")
pdf.body("EAP access: Call 1800 555 234 (24/7) or visit eap.acmecorp.internal (corporate network only). "
    "All interactions are strictly confidential and no information is disclosed to Acme Corp.")

pdf.subsection("9.2 Workplace Injury")
pdf.clause("9.2.1", "Any workplace injury must be reported to the employee's manager and the People & "
    "Culture team within 1 business day of the incident, regardless of severity.")
pdf.clause("9.2.2", "Acme Corp maintains workers' compensation insurance in all jurisdictions of "
    "operation. Injured employees are entitled to support under the applicable state scheme.")
pdf.clause("9.2.3", "Employees required to perform modified duties during recovery will be accommodated "
    "where operationally feasible. Modified duties will be reviewed fortnightly by the WHS team.")

pdf.subsection("9.3 Wellbeing Allowance")
pdf.body("All permanent employees receive an annual Wellbeing Allowance of $600 AUD (Full-Time) or "
    "$300 AUD (Part-Time), to be spent on eligible health and wellness activities. Eligible categories "
    "include: gym memberships, fitness equipment, mental health apps, nutrition coaching, and mindfulness "
    "programmes. The allowance must be claimed via the HR portal with receipts. It does not roll over "
    "and expires on 31 December each year. Casual employees are not eligible.")

# --- SECTION 10: TERMINATION ---
pdf.add_page()
pdf.section_title("Section 10: Termination & Redundancy")
pdf.subsection("10.1 Notice Periods - Resignation")
notice = [
    ("Less than 1 year", "2 weeks"),
    ("1-3 years", "3 weeks"),
    ("3-5 years", "4 weeks"),
    ("5+ years", "5 weeks"),
]
pdf.set_font("Helvetica", "B", 9)
pdf.cell(80, 7, "Length of Service", border=1)
pdf.cell(0, 7, "Notice Period (Resignation)", border=1, ln=True)
pdf.set_font("Helvetica", "", 9)
for service, notice_period in notice:
    pdf.cell(80, 7, service, border=1)
    pdf.cell(0, 7, notice_period, border=1, ln=True)
pdf.ln(4)
pdf.body("Acme Corp may elect to pay out the notice period in lieu at its discretion. If the employee "
    "fails to provide the required notice, the corresponding amount may be deducted from final pay "
    "as per the Fair Work Act 2009.")

pdf.subsection("10.2 Redundancy Payments")
pdf.body("In the event of genuine redundancy, employees are entitled to redundancy pay as prescribed "
    "by the National Employment Standards (NES), summarised below:")
redundancy = [
    ("Less than 1 year", "NIL"),
    ("1-2 years", "4 weeks"),
    ("2-3 years", "6 weeks"),
    ("3-4 years", "7 weeks"),
    ("4-5 years", "8 weeks"),
    ("5-6 years", "10 weeks"),
    ("6-7 years", "11 weeks"),
    ("7-8 years", "13 weeks"),
    ("8-9 years", "14 weeks"),
    ("9-10 years", "16 weeks"),
    ("10+ years", "12 weeks"),
]
pdf.set_font("Helvetica", "B", 9)
pdf.cell(80, 7, "Length of Service", border=1)
pdf.cell(0, 7, "Redundancy Pay", border=1, ln=True)
pdf.set_font("Helvetica", "", 9)
for service, pay in redundancy:
    pdf.cell(80, 7, service, border=1)
    pdf.cell(0, 7, pay, border=1, ln=True)
pdf.ln(4)
pdf.body("IMPORTANT: Acme Corp enhances the NES minimum by providing an additional 2 weeks of pay "
    "for each completed year of service beyond 5 years, capped at a maximum total redundancy payment "
    "of 26 weeks' pay. This enhancement is not available to employees dismissed for misconduct.")

# --- APPENDIX A ---
pdf.add_page()
pdf.section_title("Appendix A: Benefit Entitlements by Level")
pdf.body("The following summarises benefit entitlements across all employee levels. "
    "All dollar amounts are in AUD and are reviewed annually.")
benefits = [
    ("Annual Leave", "20 days", "20 days", "20 days", "20 days", "20 days", "20 days"),
    ("Leave Loading", "17.5%", "17.5%", "17.5%", "17.5%", "N/A", "N/A"),
    ("Wellbeing Allowance", "$600", "$600", "$600", "$600", "$600", "$600"),
    ("Home Office Allowance", "$800", "$800", "$800", "$800", "$800", "$800"),
    ("Laptop Refresh", "3 years", "3 years", "3 years", "3 years", "2 years", "2 years"),
    ("Phone Allowance/month", "$0", "$30", "$30", "$60", "$100", "$150"),
    ("Max Meal (client)", "$120pp", "$120pp", "$120pp", "$120pp", "$250pp", "$250pp"),
    ("Max Bonus", "5%", "5%", "10%", "10%", "20%", "30%+LTIP"),
    ("Flight Entitlement", "Economy", "Economy", "Economy", "Economy", "Bus (4h+)", "Bus (all)"),
]
col_widths = [52, 22, 22, 22, 22, 22, 22]
headers = ["Benefit", "L1", "L2", "L3", "L4", "L5", "L6"]
pdf.set_font("Helvetica", "B", 8)
for i, h in enumerate(headers):
    pdf.cell(col_widths[i], 7, h, border=1, align="C")
pdf.ln()
pdf.set_font("Helvetica", "", 8)
for row in benefits:
    for i, val in enumerate(row):
        pdf.cell(col_widths[i], 7, val, border=1, align="C")
    pdf.ln()
pdf.ln(4)
pdf.body("Note: Laptop refresh cycles are approximate and subject to device condition assessment. "
    "Phone allowances are provided as a salary supplement and are taxable. Home office allowance "
    "is a one-time payment at commencement only (not per year).")

# --- APPENDIX B ---
pdf.add_page()
pdf.section_title("Appendix B: Approved Vendors & Travel Policy")
pdf.subsection("B.1 Preferred Travel Providers")
pdf.body("Acme Corp has negotiated rates with the following preferred providers. Use of preferred "
    "providers is mandatory except where operationally impractical:")
vendors = [
    ("Flights", "Qantas Business", "qantas.com/acme", "Must book 7+ days in advance for savings"),
    ("Hotels", "Marriott / IHG", "acme.marriott.com", "Corporate rate: up to 25% discount"),
    ("Car Rental", "Hertz", "hertz.com/acme-corp", "Class C (mid-size) maximum"),
    ("Rideshare", "Uber for Business", "Via Uber app", "Set up through IT; receipts auto-sync"),
    ("FX / Cash", "Wex Travel Card", "wex.com.au", "Must be activated 5 days prior to travel"),
]
pdf.set_font("Helvetica", "B", 8.5)
pdf.cell(30, 7, "Category", border=1)
pdf.cell(40, 7, "Provider", border=1)
pdf.cell(45, 7, "Booking Portal", border=1)
pdf.cell(0, 7, "Notes", border=1, ln=True)
pdf.set_font("Helvetica", "", 8.5)
for cat, prov, portal, note in vendors:
    pdf.cell(30, 7, cat, border=1)
    pdf.cell(40, 7, prov, border=1)
    pdf.cell(45, 7, portal, border=1)
    pdf.cell(0, 7, note, border=1, ln=True)
pdf.ln(4)

pdf.subsection("B.2 Non-Approved Expenditure")
pdf.body("The following are explicitly non-reimbursable: personal entertainment (movies, sports events "
    "not for client purposes), alcohol consumed alone, fines or penalties, personal subscriptions, "
    "first-class flights for any level, luggage above 23kg on domestic flights, and any expense "
    "that violates the Code of Conduct.")

pdf.subsection("B.3 End of Year Note")
pdf.body("All expense claims for any financial year (ending 30 June) must be submitted by 31 July. "
    "Claims submitted after this date will be processed in the following financial year. This cutoff "
    "is a hard deadline and no exceptions will be granted after the Finance team closes the books.")

fname = "acme_corp_policy_manual.pdf"
pdf.output(fname)
print(f"PDF generated: {fname} ({pdf.page_no()} pages)")
