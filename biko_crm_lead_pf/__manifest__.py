# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "BIKO: Report docx for lead",
    "summary": "PF docx for lead",
    "author": "Zhmihova T.N.",
    "company": "BIKO Solutions",
    "category": "Reporting",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [        
        "crm",
        "web",
        "biko_report_docx",
        "biko_crm_lead_total",
        ],    
    "data": [        
        "views/pf_template.xml",
        "report/lead_pf_report.xml",
        "security/ir.model.access.csv",
        "data/data_template.xml",
        ],
    "installable": True,
}
