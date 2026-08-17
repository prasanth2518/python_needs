paylaods = {"BCEE": {
    "docList": [
        {
            "uploadedDocument": {
                "documentId": "DOC-001",
                "fileName": "birth_certificate_pass.pdf",
                "fileRef": {
                    "fileId": "birth_certificate_pass"
                },
                "metadata": {
                    "mimeType": "application/pdf",
                    "sizeBytes": 524288
                },
                "uploadTime": {
                    "asOf": "2026-08-12T10:00:00-07:00",
                    "timezone": "Pacific Daylight Time"
                }
            },
            "result": {
                "classifications": [
                    {
                        "documentType": "BIRTH_CERTIFICATE",
                        "reasoning": "Official birth certificate showing child name, date of birth, parent names, and state certification.",
                        "matchedDependent": "DEP-002",
                        "pageRange": [
                            1
                        ],
                        "verificationStatus": "PASS",
                        "verificationCode": "1000",
                        "validationDetails": {
                            "childName": {
                                "extracted": "Tommy",
                                "DEP-002": {
                                    "submitted": "Tommy",
                                    "field_match_status": "PASS"
                                }
                            },
                            "childDob": {
                                "extracted": "2015-08-22",
                                "DEP-002": {
                                    "submitted": "2015-08-22",
                                    "field_match_status": "PASS"
                                }
                            },
                            "parentNames": {
                                "extracted": [
                                    "John",
                                    "Jane"
                                ],
                                "comparisons": {
                                    "submitter": {
                                        "submitted": "John",
                                        "matchedExtracted": "John",
                                        "field_match_status": "PASS"
                                    },
                                    "spouseOrDp": {
                                        "submitted": "Jane",
                                        "matchedExtracted": "Jane",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "matchedAgainst": [
                                    "submitter",
                                    "spouseOrDp"
                                ],
                                "field_match_status": "PASS"
                            },
                            "officialSigned": {
                                "extracted": "yes",
                                "reasoning": "The certificate shows a visible state registrar certification and official signature.",
                                "field_match_status": "PASS"
                            }
                        },
                        "comment": "All standardized checks passed for BIRTH_CERTIFICATE."
                    }
                ]
            }
        }
    ]
},

    "BC": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-001",
                    "fileName": "birth_certificate_pass.pdf",
                    "fileRef": {
                        "fileId": "birth_certificate_pass"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 524288
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:00:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "BIRTH_CERTIFICATE",
                            "reasoning": "Official birth certificate showing child name, date of birth, parent names, and state certification.",
                            "matchedDependent": "DEP-002",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "PASS",
                            "verificationCode": "1000",
                            "validationDetails": {
                                "childName": {
                                    "extracted": "Tommy",
                                    "DEP-002": {
                                        "submitted": "Tommy",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "childDob": {
                                    "extracted": "2015-08-22",
                                    "DEP-002": {
                                        "submitted": "2015-08-22",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "parentNames": {
                                    "extracted": [
                                        "Jane"
                                    ],
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "matchedExtracted": None,
                                            "field_match_status": "FAIL"
                                        },
                                        "spouseOrDp": {
                                            "submitted": "Jane",
                                            "matchedExtracted": "Jane",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": [
                                        "spouseOrDp"
                                    ],
                                    "field_match_status": "PASS"
                                },
                                "officialSigned": {
                                    "extracted": "yes",
                                    "reasoning": "The certificate shows a visible state registrar certification and official signature.",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "All standardized checks passed for BIRTH_CERTIFICATE."
                        }
                    ]
                }
            }
        ]
    },

    "IBC": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-002",
                    "fileName": "birth_certificate_fail.pdf",
                    "fileRef": {
                        "fileId": "birth_certificate_fail"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 532480
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:05:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "BIRTH_CERTIFICATE",
                            "reasoning": "Official birth certificate showing a different child and unrelated parents.",
                            "matchedDependent": "DEP-003",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "FAIL",
                            "verificationCode": "2000",
                            "validationDetails": {
                                "childName": {
                                    "extracted": "George",
                                    "DEP-003": {
                                        "submitted": "Lucas",
                                        "field_match_status": "FAIL"
                                    }
                                },
                                "childDob": {
                                    "extracted": "2018-08-22",
                                    "DEP-003": {
                                        "submitted": "2017-01-15",
                                        "field_match_status": "FAIL"
                                    }
                                },
                                "parentNames": {
                                    "extracted": [
                                        "Mary",
                                        "Robert"
                                    ],
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "matchedExtracted": None,
                                            "field_match_status": "FAIL"
                                        },
                                        "spouseOrDp": {
                                            "submitted": "Jane",
                                            "matchedExtracted": None,
                                            "field_match_status": "FAIL"
                                        }
                                    },
                                    "matchedAgainst": [],
                                    "field_match_status": "FAIL"
                                },
                                "officialSigned": {
                                    "extracted": "yes",
                                    "reasoning": "The document appears state-certified, but the child and parent information do not match the payload.",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "Standardized verification failed for BIRTH_CERTIFICATE because childName, childDob, parentNames did not match."
                        }
                    ]
                }
            }
        ]
    },

    "MC": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-003",
                    "fileName": "marriage_certificate_pass.pdf",
                    "fileRef": {
                        "fileId": "marriage_certificate_pass"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 487424
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:10:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "MARRIAGE_CERTIFICATE",
                            "reasoning": "Marriage certificate showing both parties, ceremony date, and officiant signature.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "PASS",
                            "verificationCode": "1000",
                            "validationDetails": {
                                "submitterName": {
                                    "extracted": "John",
                                    "submitted": "John",
                                    "field_match_status": "PASS"
                                },
                                "dependentName": {
                                    "extracted": "Jane",
                                    "DEP-001": {
                                        "submitted": "Jane",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "marriageDatePresent": {
                                    "extracted": "2010-06-15",
                                    "reasoning": "The ceremony date is fully visible in the marriage section of the certificate.",
                                    "field_match_status": "PASS"
                                },
                                "officiantSigned": {
                                    "extracted": "yes",
                                    "reasoning": "A qualifying officiant signature is clearly visible in the completed marriage section.",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "All standardized checks passed for MARRIAGE_CERTIFICATE."
                        }
                    ]
                }
            }
        ]
    },

    "IMC": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-004",
                    "fileName": "marriage_certificate_fail.pdf",
                    "fileRef": {
                        "fileId": "marriage_certificate_fail"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 493568
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:15:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "MARRIAGE_CERTIFICATE",
                            "reasoning": "Marriage license showing both parties but no completed ceremony date and no qualifying officiant signature in the completed marriage section.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "FAIL",
                            "verificationCode": "2000",
                            "validationDetails": {
                                "submitterName": {
                                    "extracted": "John",
                                    "submitted": "John",
                                    "field_match_status": "PASS"
                                },
                                "dependentName": {
                                    "extracted": "Jane",
                                    "DEP-001": {
                                        "submitted": "Jane",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "marriageDatePresent": {
                                    "extracted": None,
                                    "reasoning": "Only the license issuance information is visible; the completed ceremony date is blank.",
                                    "field_match_status": "FAIL"
                                },
                                "officiantSigned": {
                                    "extracted": "no",
                                    "reasoning": "The completed marriage section is visible and unsigned; only issuance-side signatures are present.",
                                    "field_match_status": "FAIL"
                                }
                            },
                            "comment": "Standardized verification failed for MARRIAGE_CERTIFICATE because marriageDatePresent, officiantSigned did not match."
                        }
                    ]
                }
            }
        ]
    },

    "SMC": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-005",
                    "fileName": "state_issued_marriage_certificate_pass.pdf",
                    "fileRef": {
                        "fileId": "state_issued_marriage_certificate_pass"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 501760
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:20:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "STATE_ISSUED_MARRIAGE_CERTIFICATE",
                            "reasoning": "County-issued marriage certificate showing both parties, ceremony date, officiant signature, and government issuance markings.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "PASS",
                            "verificationCode": "1000",
                            "validationDetails": {
                                "submitterName": {
                                    "extracted": "John",
                                    "submitted": "John",
                                    "field_match_status": "PASS"
                                },
                                "dependentName": {
                                    "extracted": "Jane",
                                    "DEP-001": {
                                        "submitted": "Jane",
                                        "field_match_status": "PASS"
                                    }
                                },
                                "marriageDatePresent": {
                                    "extracted": "2010-06-15",
                                    "reasoning": "The certificate clearly shows the completed ceremony date in the solemnization section.",
                                    "field_match_status": "PASS"
                                },
                                "officiantSigned": {
                                    "extracted": "yes",
                                    "reasoning": "The officiant signature and county certification are both clearly visible.",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "All standardized checks passed for STATE_ISSUED_MARRIAGE_CERTIFICATE."
                        }
                    ]
                }
            }
        ]
    },

    "1040": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-006",
                    "fileName": "tax_return_1040_mfj_pass.pdf",
                    "fileRef": {
                        "fileId": "tax_return_1040_mfj_pass"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 786432
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:25:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "TAX_RETURN_1040",
                            "reasoning": "Official IRS Form 1040 showing tax year, married filing jointly status, and both filer name fields.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "PASS",
                            "verificationCode": "1000",
                            "validationDetails": {
                                "filingStatus": {
                                    "extracted": "MFJ",
                                    "field_match_status": "PASS"
                                },
                                "taxYear": {
                                    "extracted": "2025",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerFirstName": {
                                    "extracted": "John",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Jane",
                                            "field_match_status": "FAIL"
                                        }
                                    },
                                    "matchedAgainst": "submitter",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "submitter",
                                    "field_match_status": "PASS"
                                },
                                "spouseFieldFirstName": {
                                    "extracted": "Jane",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "field_match_status": "FAIL"
                                        },
                                        "DEP-001": {
                                            "submitted": "Jane",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "DEP-001",
                                    "field_match_status": "PASS"
                                },
                                "spouseFieldLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "DEP-001",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "All standardized checks passed for TAX_RETURN_1040."
                        }
                    ]
                }
            }
        ]
    },

    "ITAX": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-007",
                    "fileName": "tax_return_1040_mfs_fail.pdf",
                    "fileRef": {
                        "fileId": "tax_return_1040_mfs_fail"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 792576
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:30:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "TAX_RETURN_1040",
                            "reasoning": "Official IRS Form 1040 showing married filing separately status and filer name fields, but the spouse field does not match the payload spouse.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1
                            ],
                            "verificationStatus": "FAIL",
                            "verificationCode": "2000",
                            "validationDetails": {
                                "filingStatus": {
                                    "extracted": "MFS",
                                    "field_match_status": "PASS"
                                },
                                "taxYear": {
                                    "extracted": "2025",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerFirstName": {
                                    "extracted": "John",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Jane",
                                            "field_match_status": "FAIL"
                                        }
                                    },
                                    "matchedAgainst": "submitter",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "submitter",
                                    "field_match_status": "PASS"
                                },
                                "spouseFieldFirstName": {
                                    "extracted": "Mary",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "field_match_status": "FAIL"
                                        },
                                        "DEP-001": {
                                            "submitted": "Jane",
                                            "field_match_status": "FAIL"
                                        }
                                    },
                                    "matchedAgainst": None,
                                    "field_match_status": "FAIL"
                                },
                                "spouseFieldLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "DEP-001",
                                    "field_match_status": "PASS"
                                }
                            },
                            "comment": "Standardized verification failed for TAX_RETURN_1040 because spouseFieldFirstName did not match."
                        }
                    ]
                }
            }
        ]
    },

    "SP1040": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-008",
                    "fileName": "tax_return_1040_hoh_pass.pdf",
                    "fileRef": {
                        "fileId": "tax_return_1040_hoh_pass"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 798720
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:35:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "TAX_RETURN_1040",
                            "reasoning": "Official IRS Form 1040 showing head of household status and primary filer matching the spouse dependent.",
                            "matchedDependent": "DEP-001",
                            "pageRange": [
                                1,
                                2
                            ],
                            "verificationStatus": "PASS",
                            "verificationCode": "1000",
                            "validationDetails": {
                                "filingStatus": {
                                    "extracted": "HOH",
                                    "field_match_status": "PASS"
                                },
                                "taxYear": {
                                    "extracted": "2025",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerFirstName": {
                                    "extracted": "Jane",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "John",
                                            "field_match_status": "FAIL"
                                        },
                                        "DEP-001": {
                                            "submitted": "Jane",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "DEP-001",
                                    "field_match_status": "PASS"
                                },
                                "primaryFilerLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {
                                        "submitter": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        },
                                        "DEP-001": {
                                            "submitted": "Smith",
                                            "field_match_status": "PASS"
                                        }
                                    },
                                    "matchedAgainst": "DEP-001",
                                    "field_match_status": "PASS"
                                },
                                "spouseFieldFirstName": {
                                    "extracted": "John",
                                    "comparisons": {},
                                    "matchedAgainst": None,
                                    "field_match_status": "FAIL"
                                },
                                "spouseFieldLastName": {
                                    "extracted": "Smith",
                                    "comparisons": {},
                                    "matchedAgainst": None,
                                    "field_match_status": "FAIL"
                                }
                            },
                            "comment": "All standardized checks passed for TAX_RETURN_1040."
                        }
                    ]
                }
            }
        ]
    },

    "Other": {
        "docList": [
            {
                "uploadedDocument": {
                    "documentId": "DOC-009",
                    "fileName": "unsupported_document.pdf",
                    "fileRef": {
                        "fileId": "unsupported_document"
                    },
                    "metadata": {
                        "mimeType": "application/pdf",
                        "sizeBytes": 245760
                    },
                    "uploadTime": {
                        "asOf": "2026-08-12T10:40:00-07:00",
                        "timezone": "Pacific Daylight Time"
                    }
                },
                "result": {
                    "classifications": [
                        {
                            "documentType": "OTHER",
                            "reasoning": "Utility bill and cover sheet pages that do not match any supported validation document type.",
                            "matchedDependent": None,
                            "pageRange": [
                                1,
                                2
                            ],
                            "verificationStatus": "FAIL",
                            "verificationCode": "4000",
                            "validationDetails": {},
                            "comment": "Document is unsupported or unrelated for standardized validation."
                        }
                    ]
                }
            }
        ]
    }}



"""Label-resolution FaaS: rewrite each classification's documentType to its
canonical Final Label using rules from a MinIO-hosted Excel file.

Inputs: minio_file_path (rules .xlsx URN) and document_verification_response.
Returns the mutated document_verification_response, or a guarded error dict.
"""

import logging
import os
import re
import tempfile
import traceback
from datetime import date

logger = logging.getLogger("enso.faas.task_faas_1")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO").upper())
if not logger.handlers and not logging.getLogger().handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    )
    logger.addHandler(_handler)

_MISSING = object()  # tells an absent key apart from a stored None

_COL_AI_LABEL = "AI Document Label"
_COL_FINAL_LABEL = "Final Label"
_COL_RULES = "Rules"


def _download_from_minio(minio_urn, local_path):
    from xpms_file_storage.file_handler import XpmsResource, LocalResource  # lazy

    minio_res = XpmsResource.get(key=minio_urn)
    lcl_res = LocalResource(fullpath=local_path)
    minio_res.copy(lcl_res)


def _load_rule_rows(xlsx_path):
    """Parse the rules workbook into row dicts, in sheet order."""
    import openpyxl  # lazy

    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []

    header = [str(c).strip() if c is not None else "" for c in rows[0]]
    col = {name: idx for idx, name in enumerate(header)}
    for required in (_COL_AI_LABEL, _COL_FINAL_LABEL, _COL_RULES):
        if required not in col:
            raise ValueError(
                f"Label-rules workbook is missing the {required!r} column "
                f"(found columns: {header})"
            )

    def _cell(raw, name):
        idx = col[name]
        return raw[idx] if idx < len(raw) else None

    rule_rows = []
    for raw in rows[1:]:
        ai_label = _cell(raw, _COL_AI_LABEL)
        if ai_label is None or str(ai_label).strip() == "":
            continue

        final_label = _cell(raw, _COL_FINAL_LABEL)
        rules_cell = _cell(raw, _COL_RULES)

        # split "A OR B" so a compound cell matches either label
        ai_labels = [tok.strip() for tok in str(ai_label).split(" OR ") if tok.strip()]
        final_label = str(final_label).strip() if final_label is not None else ""

        raw_rules = []
        if rules_cell is not None:
            for line in str(rules_cell).splitlines():
                line = re.sub(r"^\s*\d+\.\s*", "", line).strip()  # drop "N. "
                if line:
                    raw_rules.append(line)

        rule_rows.append(
            {"ai_labels": ai_labels, "final_label": final_label, "rules": raw_rules}
        )

    return rule_rows


def _dig(obj, key):
    """First occurrence of key anywhere in nested dicts/lists, else _MISSING."""
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for value in obj.values():
            found = _dig(value, key)
            if found is not _MISSING:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = _dig(item, key)
            if found is not _MISSING:
                return found
    return _MISSING


def _resolve_field(classification, json_path):
    """Resolve a 'result.classifications.<...>' rule path to its value."""
    prefix = "result.classifications."
    path = json_path[len(prefix):] if json_path.startswith(prefix) else json_path
    parts = [p for p in path.split(".") if p]
    if not parts:
        return None

    # first segment: top-level field if present, else search under validationDetails
    if isinstance(classification, dict) and parts[0] in classification:
        current = classification[parts[0]]
    else:
        current = _dig(classification, parts[0])
        if current is _MISSING:
            return None

    for part in parts[1:]:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            nested = _dig(current, part)
            current = None if nested is _MISSING else nested
    return current


def _tax_year_in_valid_range(value):
    """Jan1-Apr15 -> previous two years valid; Apr16-Dec31 -> previous year only."""
    if value is None:
        return False
    match = re.search(r"\d{4}", str(value))
    if not match:
        return False
    year = int(match.group())

    today = date.today()
    current_year = today.year
    if today <= date(current_year, 4, 15):
        valid_years = {current_year - 1, current_year - 2}
    else:
        valid_years = {current_year - 1}
    return year in valid_years


def _split_operator(rule_line):
    # match != and == before a bare = (which is treated as ==)
    if "!=" in rule_line:
        lhs, rhs = rule_line.split("!=", 1)
        return lhs.strip(), "!=", rhs.strip()
    if "==" in rule_line:
        lhs, rhs = rule_line.split("==", 1)
        return lhs.strip(), "==", rhs.strip()
    if "=" in rule_line:
        lhs, rhs = rule_line.split("=", 1)
        return lhs.strip(), "==", rhs.strip()
    return None


def _matches_value(actual, expected):
    # list -> membership; scalar -> string equality
    if isinstance(actual, list):
        return expected in [str(v).strip() for v in actual]
    actual_str = "" if actual is None else str(actual).strip()
    return actual_str == expected


def _evaluate_rule_line(rule_line, classification):
    parsed = _split_operator(rule_line)
    if parsed is None:
        # logger.warning("Could not parse rule (no operator): %r", rule_line)
        return False
    json_path, op, rhs = parsed

    # date-range tokens: check NOT before IS
    rhs_upper = rhs.upper()
    if "NOT IN VALID DATE RANGE" in rhs_upper:
        in_range = _tax_year_in_valid_range(_resolve_field(classification, json_path))
        result = not in_range
        return result if op == "==" else not result
    if "IN VALID DATE RANGE" in rhs_upper:
        in_range = _tax_year_in_valid_range(_resolve_field(classification, json_path))
        return in_range if op == "==" else not in_range

    # quoted value(s), possibly "A" OR "B"
    expected_values = []
    for part in re.split(r"\s+OR\s+", rhs):
        part = part.strip()
        if len(part) >= 2 and part[0] == '"' and part[-1] == '"':
            part = part[1:-1]
        if part:
            expected_values.append(part)

    actual = _resolve_field(classification, json_path)
    any_match = any(_matches_value(actual, ev) for ev in expected_values)
    return any_match if op == "==" else not any_match


def _rules_satisfied(rule_row, classification):
    # every rule in the row must hold
    for rule_line in rule_row["rules"]:
        if not _evaluate_rule_line(rule_line, classification):
            return False
    return True


def _resolve_final_label(retrieved_document_label, rule_rows, classification):
    # candidate rows in sheet order; first row whose rules all hold wins
    for rule_row in rule_rows:
        if retrieved_document_label not in rule_row["ai_labels"]:
            continue
        if _rules_satisfied(rule_row, classification):
            return rule_row["final_label"]
    return None


def task_faas_1( **input_obj):
    """Rewrite each classification's documentType to its Final Label."""
    tmp_path = None
    try:
        minio_file_path = ""
        # minio_file_path = input_obj.get("minio_file_path")
        # if not minio_file_path:
        #     raise ValueError("'minio_file_path' is required in input_obj")

        document_verification_response = input_obj.get("document_verification_response")
        if not isinstance(document_verification_response, dict):
            raise ValueError(
                "'document_verification_response' must be a dict in input_obj"
            )

        doc_list = document_verification_response.get("docList")
        if not isinstance(doc_list, list):
            raise ValueError("'document_verification_response.docList' must be a list")

       # logger.info(
       #      "task_faas_1 started: minio_file_path=%s, docList length=%d",
       #      minio_file_path,
       #      len(doc_list),
       #  )

        tmp_path = "dev_label_rules.xlsx"
        # logger.info("Downloading label-rules Excel from MinIO: %s", minio_file_path)
        # _download_from_minio(minio_file_path, tmp_path)
        # logger.info("Downloaded label-rules Excel to: %s", tmp_path)

        rule_rows = _load_rule_rows(tmp_path)
        # logger.info("Loaded %d rule row(s) from Excel", len(rule_rows))

        for i, doc_entry in enumerate(doc_list):
            if not isinstance(doc_entry, dict):
                continue
            classifications = (doc_entry.get("result") or {}).get("classifications")
            if not isinstance(classifications, list):
                continue

            for j, classification in enumerate(classifications):
                if not isinstance(classification, dict):
                    continue

                retrieved_document_label = classification.get("documentType")
                if not retrieved_document_label:
                    #  logger.warning(
                    #     "docList[%d].classifications[%d] has no documentType; skipping",
                    #     i, j,
                    # )
                    continue

                final_label = _resolve_final_label(
                    retrieved_document_label, rule_rows, classification
                )

                if final_label is not None:
                    # logger.info(
                    #     "docList[%d].classifications[%d]: documentType %r -> %r",
                    #     i, j, retrieved_document_label, final_label,
                    # )
                    classification["documentType"] = final_label
                    print("SCRRIPT_LABLE",final_label)# in-place
                else:
                    pass
                     # logger.warning(
                    #     "docList[%d].classifications[%d]: no rule satisfied for %r; "
                    #     "documentType left unchanged",
                    #     i, j, retrieved_document_label,
                    # )

        # logger.info("task_faas_1 completed successfully")
        return document_verification_response,final_label

    except Exception as err:  # noqa: BLE001
        # logger.error("task_faas_1 failed: %s\n%s", err, traceback.format_exc())
        return {
            "success": False,
            "error": str(err),
            "traceback": traceback.format_exc(),
        },final_label
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                pass
                # os.remove(tmp_path)
                # logger.info("Removed temp file %s", tmp_path)
            except OSError as cleanup_err:
                pass
                # logger.error("Failed to remove temp file %s: %s", tmp_path, cleanup_err)


for i in paylaods:
    print("ACTUAL_LABLE",i)
    j = {"document_verification_response":paylaods[i]}
    dvr,final_lable = task_faas_1(**j)
    if final_lable == i:
        print("test_passed",final_lable)
    else:
        print("test_failed",final_lable)
    print("===============================")