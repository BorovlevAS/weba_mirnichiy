# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Base report docx",
    "summary": "Base module to create docx report",
    "author": "Zhmihova T.N.",
    "company": "BIKO Solutions",
    "category": "Reporting",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "base",
        "web"
        ],   
    "data": [
        "views/webclient_templates.xml",
        ],
    "external_dependencies": {
        "python": ['docxtpl'],
        },
    "installable": True,
}
