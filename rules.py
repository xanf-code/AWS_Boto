response = client.create_rule_group(
    Name='string',
    Scope='CLOUDFRONT'|'REGIONAL',
    Capacity=123,
    Description='string',
    Rules=[
        {
            'Name': 'string',
            'Priority': 123,
            'Statement': {
                'ByteMatchStatement': {
                    'SearchString': b'bytes',
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ],
                    'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                },
                'SqliMatchStatement': {
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ],
                    'SensitivityLevel': 'LOW'|'HIGH'
                },
                'XssMatchStatement': {
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ]
                },
                'SizeConstraintStatement': {
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                    'Size': 123,
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ]
                },
                'GeoMatchStatement': {
                    'CountryCodes': [
                        'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'|'XK',
                    ],
                    'ForwardedIPConfig': {
                        'HeaderName': 'string',
                        'FallbackBehavior': 'MATCH'|'NO_MATCH'
                    }
                },
                'RuleGroupReferenceStatement': {
                    'ARN': 'string',
                    'ExcludedRules': [
                        {
                            'Name': 'string'
                        },
                    ]
                },
                'IPSetReferenceStatement': {
                    'ARN': 'string',
                    'IPSetForwardedIPConfig': {
                        'HeaderName': 'string',
                        'FallbackBehavior': 'MATCH'|'NO_MATCH',
                        'Position': 'FIRST'|'LAST'|'ANY'
                    }
                },
                'RegexPatternSetReferenceStatement': {
                    'ARN': 'string',
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ]
                },
                'RateBasedStatement': {
                    'Limit': 123,
                    'AggregateKeyType': 'IP'|'FORWARDED_IP',
                    'ScopeDownStatement': {'... recursive ...'},
                    'ForwardedIPConfig': {
                        'HeaderName': 'string',
                        'FallbackBehavior': 'MATCH'|'NO_MATCH'
                    }
                },
                'AndStatement': {
                    'Statements': [
                        {'... recursive ...'},
                    ]
                },
                'OrStatement': {
                    'Statements': [
                        {'... recursive ...'},
                    ]
                },
                'NotStatement': {
                    'Statement': {'... recursive ...'}
                },
                'ManagedRuleGroupStatement': {
                    'VendorName': 'string',
                    'Name': 'string',
                    'Version': 'string',
                    'ExcludedRules': [
                        {
                            'Name': 'string'
                        },
                    ],
                    'ScopeDownStatement': {'... recursive ...'},
                    'ManagedRuleGroupConfigs': [
                        {
                            'LoginPath': 'string',
                            'PayloadType': 'JSON'|'FORM_ENCODED',
                            'UsernameField': {
                                'Identifier': 'string'
                            },
                            'PasswordField': {
                                'Identifier': 'string'
                            }
                        },
                    ]
                },
                'LabelMatchStatement': {
                    'Scope': 'LABEL'|'NAMESPACE',
                    'Key': 'string'
                },
                'RegexMatchStatement': {
                    'RegexString': 'string',
                    'FieldToMatch': {
                        'SingleHeader': {
                            'Name': 'string'
                        },
                        'SingleQueryArgument': {
                            'Name': 'string'
                        },
                        'AllQueryArguments': {}
                        ,
                        'UriPath': {}
                        ,
                        'QueryString': {}
                        ,
                        'Body': {
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Method': {}
                        ,
                        'JsonBody': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedPaths': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'InvalidFallbackBehavior': 'MATCH'|'NO_MATCH'|'EVALUATE_AS_STRING',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Headers': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedHeaders': [
                                    'string',
                                ],
                                'ExcludedHeaders': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        },
                        'Cookies': {
                            'MatchPattern': {
                                'All': {}
                                ,
                                'IncludedCookies': [
                                    'string',
                                ],
                                'ExcludedCookies': [
                                    'string',
                                ]
                            },
                            'MatchScope': 'ALL'|'KEY'|'VALUE',
                            'OversizeHandling': 'CONTINUE'|'MATCH'|'NO_MATCH'
                        }
                    },
                    'TextTransformations': [
                        {
                            'Priority': 123,
                            'Type': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'|'BASE64_DECODE'|'HEX_DECODE'|'MD5'|'REPLACE_COMMENTS'|'ESCAPE_SEQ_DECODE'|'SQL_HEX_DECODE'|'CSS_DECODE'|'JS_DECODE'|'NORMALIZE_PATH'|'NORMALIZE_PATH_WIN'|'REMOVE_NULLS'|'REPLACE_NULLS'|'BASE64_DECODE_EXT'|'URL_DECODE_UNI'|'UTF8_TO_UNICODE'
                        },
                    ]
                }
            },
            'Action': {
                'Block': {
                    'CustomResponse': {
                        'ResponseCode': 123,
                        'CustomResponseBodyKey': 'string',
                        'ResponseHeaders': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'Allow': {
                    'CustomRequestHandling': {
                        'InsertHeaders': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'Count': {
                    'CustomRequestHandling': {
                        'InsertHeaders': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'Captcha': {
                    'CustomRequestHandling': {
                        'InsertHeaders': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                }
            },
            'OverrideAction': {
                'Count': {
                    'CustomRequestHandling': {
                        'InsertHeaders': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    }
                },
                'None': {}

            },
            'RuleLabels': [
                {
                    'Name': 'string'
                },
            ],
            'VisibilityConfig': {
                'SampledRequestsEnabled': True|False,
                'CloudWatchMetricsEnabled': True|False,
                'MetricName': 'string'
            },
            'CaptchaConfig': {
                'ImmunityTimeProperty': {
                    'ImmunityTime': 123
                }
            }
        },
    ],
    VisibilityConfig={
        'SampledRequestsEnabled': True|False,
        'CloudWatchMetricsEnabled': True|False,
        'MetricName': 'string'
    },
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    CustomResponseBodies={
        'string': {
            'ContentType': 'TEXT_PLAIN'|'TEXT_HTML'|'APPLICATION_JSON',
            'Content': 'string'
        }
    }
)