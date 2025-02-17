#
# Wordless: Settings - Global Settings
#
# Copyright (C) 2018-2021  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

from wl_measures import (
    wl_measures_adjusted_freq,
    wl_measures_dispersion,
    wl_measures_effect_size,
    wl_measures_statistical_significance
)

def init_settings_global(main):
    font_size_custom = main.settings_custom['general']['font_settings']['font_size']

    main.settings_global = {
        'langs': {
            main.tr('Afrikaans'): 'afr',
            main.tr('Albanian'): 'sqi',
            main.tr('Amharric'): 'amh',
            main.tr('Arabic'): 'ara',
            main.tr('Aragonese'): 'arg',
            main.tr('Armenian'): 'hye',
            main.tr('Assamese'): 'asm',
            main.tr('Asturian'): 'ast',
            main.tr('Azerbaijani'): 'aze',
            main.tr('Basque'): 'eus',
            main.tr('Belarusian'): 'bel',
            main.tr('Bengali'): 'ben',
            main.tr('Bosnian'): 'bos',
            main.tr('Breton'): 'bre',
            main.tr('Bulgarian'): 'bul',
            main.tr('Catalan'): 'cat',
            main.tr('Chinese (Simplified)'): 'zho_cn',
            main.tr('Chinese (Traditional)'): 'zho_tw',
            main.tr('Croatian'): 'hrv',
            main.tr('Czech'): 'ces',
            main.tr('Danish'): 'dan',
            main.tr('Dutch'): 'nld',
            main.tr('Dzongkha'): 'dzo',
            main.tr('English'): 'eng',
            main.tr('Esperanto'): 'epo',
            main.tr('Estonian'): 'est',
            main.tr('Faroese'): 'fao',
            main.tr('Finnish'): 'fin',
            main.tr('French'): 'fra',
            main.tr('Galician'): 'glg',
            main.tr('Georgian'): 'kat',
            main.tr('German'): 'deu',
            main.tr('Greek (Ancient)'): 'grc',
            main.tr('Greek (Modern)'): 'ell',
            main.tr('Gujarati'): 'guj',
            main.tr('Haitian'): 'hat',
            main.tr('Hausa'): 'hau',
            main.tr('Hebrew'): 'heb',
            main.tr('Hindi'): 'hin',
            main.tr('Hungarian'): 'hun',
            main.tr('Icelandic'): 'isl',
            main.tr('Indonesian'): 'ind',
            main.tr('Irish'): 'gle',
            main.tr('Italian'): 'ita',
            main.tr('Japanese'): 'jpn',
            main.tr('Javanese'): 'jav',
            main.tr('Kannada'): 'kan',
            main.tr('Kazakh'): 'kaz',
            main.tr('Khmer'): 'khm',
            main.tr('Kinyarwanda'): 'kin',
            main.tr('Korean'): 'kor',
            main.tr('Kurdish'): 'kur',
            main.tr('Kyrgyz'): 'kir',
            main.tr('Lao'): 'lao',
            main.tr('Latin'): 'lat',
            main.tr('Latvian'): 'lav',
            main.tr('Ligurian'): 'lij',
            main.tr('Lithuanian'): 'lit',
            main.tr('Luxembourgish'): 'ltz',
            main.tr('Macedonian'): 'mkd',
            main.tr('Malagasy'): 'mlg',
            main.tr('Malay'): 'msa',
            main.tr('Malayalam'): 'mal',
            main.tr('Maltese'): 'mlt',
            main.tr('Manx'): 'glv',
            main.tr('Marathi'): 'mar',
            main.tr('Mongolian'): 'mon',
            main.tr('Nepali'): 'nep',
            main.tr('Norwegian Bokmål'): 'nob',
            main.tr('Norwegian Nynorsk'): 'nno',
            main.tr('Occitan'): 'oci',
            main.tr('Oriya'): 'ori',
            main.tr('Pashto'): 'pus',
            main.tr('Persian'): 'fas',
            main.tr('Polish'): 'pol',
            main.tr('Portuguese'): 'por',
            main.tr('Punjabi'): 'pan',
            main.tr('Quechua'): 'que',
            main.tr('Romanian'): 'ron',
            main.tr('Russian'): 'rus',
            main.tr('Sami (Northern)'): 'sme',
            main.tr('Scottish Gaelic'): 'gla',
            main.tr('Serbian (Cyrillic)'): 'srp_cyrl',
            main.tr('Serbian (Latin)'): 'srp_latn',
            main.tr('Sinhala'): 'sin',
            main.tr('Slovak'): 'slk',
            main.tr('Slovenian'): 'slv',
            main.tr('Somali'): 'som',
            main.tr('Sotho (Southern)'): 'sot',
            main.tr('Spanish'): 'spa',
            main.tr('Swahili'): 'swa',
            main.tr('Swedish'): 'swe',
            main.tr('Tagalog'): 'tgl',
            main.tr('Tajik'): 'tgk',
            main.tr('Tamil'): 'tam',
            main.tr('Tatar'): 'tat',
            main.tr('Telugu'): 'tel',
            main.tr('Thai'): 'tha',
            main.tr('Tibetan'): 'bod',
            main.tr('Turkish'): 'tur',
            main.tr('Ukrainian'): 'ukr',
            main.tr('Urdu'): 'urd',
            main.tr('Uyghur'): 'uig',
            main.tr('Vietnamese'): 'vie',
            main.tr('Volapük'): 'vol',
            main.tr('Walloon'): 'wln',
            main.tr('Welsh'): 'cym',
            main.tr('Xhosa'): 'xho',
            main.tr('Yoruba'): 'yor',
            main.tr('Zulu'): 'zul',

            main.tr('Other Languages'): 'other'
        },

        'lang_codes': {
            'afr': 'af',
            'amh': 'am',
            'ara': 'ar',
            'arg': 'an',
            'asm': 'as',
            'ast': 'ast',
            'aze': 'az',
            'bel': 'be',
            'ben': 'bn',
            'bod': 'bo',
            'bos': 'bs',
            'bre': 'br',
            'bul': 'bg',
            'cat': 'ca',
            'ces': 'cs',
            'cym': 'cy',
            'dan': 'da',
            'deu': 'de',
            'dzo': 'dz',
            'ell': 'el',
            'eng': 'en',
            'epo': 'eo',
            'est': 'et',
            'eus': 'eu',
            'fao': 'fo',
            'fas': 'fa',
            'fin': 'fi',
            'fra': 'fr',
            'gla': 'gd',
            'gle': 'ga',
            'glg': 'gl',
            'glv': 'gv',
            'grc': 'grc',
            'guj': 'gu',
            'hat': 'ht',
            'hau': 'ha',
            'heb': 'he',
            'hin': 'hi',
            'hrv': 'hr',
            'hun': 'hu',
            'hye': 'hy',
            'isl': 'is',
            'ind': 'id',
            'ita': 'it',
            'jav': 'jv',
            'jpn': 'ja',
            'kan': 'kn',
            'kat': 'ka',
            'kaz': 'kk',
            'khm': 'km',
            'kin': 'rw',
            'kir': 'ky',
            'kor': 'ko',
            'kur': 'ku',
            'lao': 'lo',
            'lat': 'la',
            'lav': 'lv',
            'lij': 'lij',
            'lit': 'lt',
            'ltz': 'lb',
            'mal': 'ml',
            'mar': 'mr',
            'mkd': 'mk',
            'mlg': 'mg',
            'mlt': 'mt',
            'mon': 'mn',
            'msa': 'ms',
            'nep': 'ne',
            'nld': 'nl',
            'nno': 'nn',
            'nob': 'nb',
            'oci': 'oc',
            'ori': 'or',
            'pan': 'pa',
            'pol': 'pl',
            'por': 'pt',
            'pus': 'ps',
            'que': 'qu',
            'ron': 'ro',
            'rus': 'ru',
            'sin': 'si',
            'slk': 'sk',
            'slv': 'sl',
            'sme': 'se',
            'som': 'so',
            'sot': 'st',
            'spa': 'es',
            'sqi': 'sq',
            'srp_cyrl': 'sr_cyrl',
            'srp_latn': 'sr_latn',
            'swa': 'sw',
            'swe': 'sv',
            'tam': 'ta',
            'tat': 'tt',
            'tel': 'te',
            'tgk': 'tg',
            'tgl': 'tl',
            'tha': 'th',
            'tur': 'tr',
            'uig': 'ug',
            'ukr': 'uk',
            'urd': 'ur',
            'vie': 'vi',
            'vol': 'vo',
            'wln': 'wa',
            'xho': 'xh',
            'yor': 'yo',
            'zho_cn': 'zh_cn',
            'zho_tw': 'zh_tw',
            'zul': 'zu',

            'other': 'other',
        },

        'file_encodings': {
            main.tr('All Languages (UTF-8 without BOM)'): 'utf_8',
            main.tr('All Languages (UTF-8 with BOM)'): 'utf_8_sig',
            main.tr('All Languages (UTF-16 with BOM)'): 'utf_16',
            main.tr('All Languages (UTF-16BE without BOM)'): 'utf_16_be',
            main.tr('All Languages (UTF-16LE without BOM)'): 'utf_16_le',
            main.tr('All Languages (UTF-32 with BOM)'): 'utf_32',
            main.tr('All Languages (UTF-32BE without BOM)'): 'utf_32_be',
            main.tr('All Languages (UTF-32LE without BOM)'): 'utf_32_le',
            main.tr('All Languages (UTF-7)'): 'utf_7',
            main.tr('All Languages (CP65001)'): 'cp65001',

            main.tr('Arabic (CP720)'): 'cp720',
            main.tr('Arabic (CP864)'): 'cp864',
            main.tr('Arabic (ISO-8859-6)'): 'iso8859_6',
            main.tr('Arabic (Mac OS Arabic)'): 'mac_arabic',
            main.tr('Arabic (Windows-1256)'): 'cp1256',

            main.tr('Baltic Languages (CP775)'): 'cp775',
            main.tr('Baltic Languages (ISO-8859-13)'): 'iso8859_13',
            main.tr('Baltic Languages (Windows-1257)'): 'cp1257',

            main.tr('Celtic Languages (ISO-8859-14)'): 'iso8859_14',

            main.tr('Central European (CP852)'): 'cp852',
            main.tr('Central European (ISO-8859-2)'): 'iso8859_2',
            main.tr('Central European (Mac OS Central European)'): 'mac_latin2',
            main.tr('Central European (Windows-1250)'): 'cp1250',

            main.tr('Chinese (GB18030)'): 'gb18030',
            main.tr('Chinese (GBK)'): 'gbk',

            main.tr('Chinese (Simplified) (GB2312)'): 'gb2312',
            main.tr('Chinese (Simplified) (HZ)'): 'hz_gb_2312',

            main.tr('Chinese (Traditional) (Big-5)'): 'big5',
            main.tr('Chinese (Traditional) (Big5-HKSCS)'): 'big5hkscs',
            main.tr('Chinese (Traditional) (CP950)'): 'cp950',

            main.tr('Croatian (Mac OS Croatian)'): 'mac_croatian',

            main.tr('Cyrillic (CP855)'): 'cp855',
            main.tr('Cyrillic (CP866)'): 'cp866',
            main.tr('Cyrillic (ISO-8859-5)'): 'iso8859_5',
            main.tr('Cyrillic (Mac OS Cyrillic)'): 'mac_cyrillic',
            main.tr('Cyrillic (Windows-1251)'): 'cp1251',

            main.tr('English (ASCII)'): 'ascii',
            main.tr('English (EBCDIC 037)'): 'cp037',
            main.tr('English (CP437)'): 'cp437',

            main.tr('Esperanto/Maltese (ISO-8859-3)'): 'iso8859_3',

            main.tr('European (HP Roman-8)'): 'hp_roman8',

            main.tr('French (CP863)'): 'cp863',

            main.tr('German (EBCDIC 273)'): 'cp273',

            main.tr('Greek (CP737)'): 'cp737',
            main.tr('Greek (CP869)'): 'cp869',
            main.tr('Greek (CP875)'): 'cp875',
            main.tr('Greek (ISO-8859-7)'): 'iso8859_7',
            main.tr('Greek (Mac OS Greek)'): 'mac_greek',
            main.tr('Greek (Windows-1253)'): 'windows_1253',

            main.tr('Hebrew (CP856)'): 'cp856',
            main.tr('Hebrew (CP862)'): 'cp862',
            main.tr('Hebrew (EBCDIC 424)'): 'cp424',
            main.tr('Hebrew (ISO-8859-8)'): 'iso8859_8',
            main.tr('Hebrew (Windows-1255)'): 'windows_1255',

            main.tr('Icelandic (CP861)'): 'cp861',
            main.tr('Icelandic (Mac OS Icelandic)'): 'mac_iceland',

            main.tr('Japanese (CP932)'): 'cp932',
            main.tr('Japanese (EUC-JP)'): 'euc_jp',
            main.tr('Japanese (EUC-JIS-2004)'): 'euc_jis_2004',
            main.tr('Japanese (EUC-JISx0213)'): 'euc_jisx0213',
            main.tr('Japanese (ISO-2022-JP)'): 'iso2022_jp',
            main.tr('Japanese (ISO-2022-JP-1)'): 'iso2022_jp_1',
            main.tr('Japanese (ISO-2022-JP-2)'): 'iso2022_jp_2',
            main.tr('Japanese (ISO-2022-JP-2004)'): 'iso2022_jp_2004',
            main.tr('Japanese (ISO-2022-JP-3)'): 'iso2022_jp_3',
            main.tr('Japanese (ISO-2022-JP-EXT)'): 'iso2022_jp_ext',
            main.tr('Japanese (Shift_JIS)'): 'shift_jis',
            main.tr('Japanese (Shift_JIS-2004)'): 'shift_jis_2004',
            main.tr('Japanese (Shift_JISx0213)'): 'shift_jisx0213',

            main.tr('Kazakh (KZ-1048)'): 'kz1048',
            main.tr('Kazakh (PTCP154)'): 'ptcp154',

            main.tr('Korean (EUC-KR)'): 'euc_kr',
            main.tr('Korean (ISO-2022-KR)'): 'iso2022_kr',
            main.tr('Korean (JOHAB)'): 'johab',
            main.tr('Korean (UHC)'): 'cp949',

            main.tr('Nordic Languages (CP865)'): 'cp865',
            main.tr('Nordic Languages (ISO-8859-10)'): 'iso8859_10',

            main.tr('North European (ISO-8859-4)'): 'iso8859_4',

            main.tr('Persian/Urdu (Mac OS Farsi)'): 'mac_farsi',

            main.tr('Portuguese (CP860)'): 'cp860',

            main.tr('Romanian (Mac OS Romanian)'): 'mac_romanian',

            main.tr('Russian (KOI8-R)'): 'koi8_r',

            main.tr('South-Eastern European (ISO-8859-16)'): 'iso8859_16',

            main.tr('Tajik (KOI8-T)'): 'koi8_t',

            main.tr('Thai (CP874)'): 'cp874',
            main.tr('Thai (ISO-8859-11)'): 'iso8859_11',
            main.tr('Thai (TIS-620)'): 'tis_620',

            main.tr('Turkish (CP857)'): 'cp857',
            main.tr('Turkish (EBCDIC 1026)'): 'cp1026',
            main.tr('Turkish (ISO-8859-9)'): 'iso8859_9',
            main.tr('Turkish (Mac OS Turkish)'): 'mac_turkish',
            main.tr('Turkish (Windows-1254)'): 'cp1254',

            main.tr('Ukrainian (CP1125)'): 'cp1125',
            main.tr('Ukrainian (KOI8-U)'): 'koi8_u',

            main.tr('Urdu (CP1006)'): 'cp1006',

            main.tr('Vietnamese (CP1258)'): 'cp1258',

            main.tr('Western European (EBCDIC 500)'): 'cp500',
            main.tr('Western European (CP850)'): 'cp850',
            main.tr('Western European (CP858)'): 'cp858',
            main.tr('Western European (CP1140)'): 'cp1140',
            main.tr('Western European (ISO-8859-1)'): 'latin_1',
            main.tr('Western European (ISO-8859-15)'): 'iso8859_15',
            main.tr('Western European (Mac OS Roman)'): 'mac_roman',
            main.tr('Western European (Windows-1252)'): 'windows_1252',
        },

        'file_types': {
            'files': [
                main.tr('Text File (*.txt)'),
                main.tr('Word Document (*.docx)'),
                main.tr('Excel Workbook (*.xlsx)'),
                main.tr('CSV File(*.csv)'),
                main.tr('HTML Page (*.htm; *.html)'),
                main.tr('XML File (*.xml)'),
                main.tr('Translation Memory File (*.tmx)'),
                main.tr('All Files (*.*)')
            ],

            'export_tables': [
                main.tr('CSV File (*.csv)'),
                main.tr('Excel Workbook (*.xlsx)')
            ],

            'export_tables_concordancer': [
                main.tr('CSV File (*.csv)'),
                main.tr('Excel Workbook (*.xlsx)'),
                main.tr('Word Document (*.docx)')
            ]
        },

        'sentence_tokenizers': {
            'afr': [
                main.tr('spaCy - Sentencizer')
            ],

            'sqi': [
                main.tr('spaCy - Sentencizer')
            ],

            'ara': [
                main.tr('spaCy - Sentencizer')
            ],

            'hye': [
                main.tr('spaCy - Sentencizer')
            ],

            'eus': [
                main.tr('spaCy - Sentencizer')
            ],

            'ben': [
                main.tr('spaCy - Sentencizer')
            ],

            'bul': [
                main.tr('spaCy - Sentencizer')
            ],

            'cat': [
                main.tr('spaCy - Sentencizer')
            ],

            'zho_cn': [
                main.tr('Wordless - Chinese Sentence Tokenizer')
            ],

            'zho_tw': [
                main.tr('Wordless - Chinese Sentence Tokenizer')
            ],

            'hrv': [
                main.tr('spaCy - Sentencizer')
            ],

            'ces': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'dan': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'nld': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'eng': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer'),
                main.tr('syntok - Sentence Segmenter')
            ],

            'est': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'fin': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'fra': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'deu': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer'),
                main.tr('syntok - Sentence Segmenter')
            ],

            'ell': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'guj': [
                main.tr('spaCy - Sentencizer')
            ],

            'heb': [
                main.tr('spaCy - Sentencizer')
            ],

            'hin': [
                main.tr('spaCy - Sentencizer')
            ],

            'hun': [
                main.tr('spaCy - Sentencizer')
            ],

            'isl': [
                main.tr('spaCy - Sentencizer'),
                main.tr('Tokenizer - Icelandic Sentence Tokenizer')
            ],

            'ind': [
                main.tr('spaCy - Sentencizer')
            ],

            'gle': [
                main.tr('spaCy - Sentencizer')
            ],

            'ita': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'jpn': [
                main.tr('Wordless - Japanese Sentence Tokenizer')
            ],

            'kan': [
                main.tr('spaCy - Sentencizer')
            ],

            'lav': [
                main.tr('spaCy - Sentencizer')
            ],

            'lij': [
                main.tr('spaCy - Sentencizer')
            ],

            'lit': [
                main.tr('spaCy - Sentencizer')
            ],

            'ltz': [
                main.tr('spaCy - Sentencizer')
            ],

            'mal': [
                main.tr('spaCy - Sentencizer')
            ],

            'nep': [
                main.tr('spaCy - Sentencizer')
            ],

            'nob': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'nno': [
                main.tr('NLTK - Punkt Sentence Tokenizer')
            ],

            'fas': [
                main.tr('spaCy - Sentencizer')
            ],

            'pol': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'por': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'ron': [
                main.tr('spaCy - Sentencizer')
            ],

            'rus': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('razdel - Russian Sentenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'sin': [
                main.tr('spaCy - Sentencizer')
            ],

            'slk': [
                main.tr('spaCy - Sentencizer')
            ],

            'slv': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'spa': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer'),
                main.tr('syntok - Sentence Segmenter')
            ],

            'swe': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'tgl': [
                main.tr('spaCy - Sentencizer')
            ],

            'tam': [
                main.tr('spaCy - Sentencizer')
            ],

            'tat': [
                main.tr('spaCy - Sentencizer')
            ],

            'tel': [
                main.tr('spaCy - Sentencizer')
            ],

            'tha': [
                main.tr('PyThaiNLP - CRFCut')
            ],

            'bod': [
                main.tr('botok - Tibetan Sentence Tokenizer')
            ],

            'tur': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer')
            ],

            'ukr': [
                main.tr('spaCy - Sentencizer')
            ],

            'urd': [
                main.tr('spaCy - Sentencizer')
            ],

            'vie': [
                main.tr('Underthesea - Vietnamese Sentence Tokenizer')
            ],

            'yor': [
                main.tr('spaCy - Sentencizer')
            ],

            'other': [
                main.tr('NLTK - Punkt Sentence Tokenizer'),
                main.tr('spaCy - Sentencizer'),
                main.tr('syntok - Sentence Segmenter')
            ]
        },

        'word_tokenizers': {
            'afr': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Afrikaans Word Tokenizer')
            ],

            'sqi': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Albanian Word Tokenizer')
            ],

            'ara': [
                main.tr('spaCy - Arabic Word Tokenizer')
            ],

            'hye': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Armenian Word Tokenizer')
            ],

            'eus': [
                main.tr('spaCy - Basque Word Tokenizer')
            ],

            'ben': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Bengali Word Tokenizer')
            ],

            'bul': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Bulgarian Word Tokenizer')
            ],

            'cat': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Catalan Word Tokenizer')
            ],

            'zho_cn': [
                main.tr('jieba - Chinese Word Tokenizer'),
                main.tr('pkuseg - Chinese Word Tokenizer'),
                main.tr('Wordless - Chinese Character Tokenizer')
            ],

            'zho_tw': [
                main.tr('jieba - Chinese Word Tokenizer'),
                main.tr('pkuseg - Chinese Word Tokenizer'),
                main.tr('Wordless - Chinese Character Tokenizer')
            ],

            'hrv': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Croatian Word Tokenizer')
            ],

            'ces': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Czech Word Tokenizer')
            ],

            'dan': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Danish Word Tokenizer')
            ],

            'nld': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Dutch Word Tokenizer')
            ],

            'eng': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - English Word Tokenizer'),
                main.tr('syntok - Word Tokenizer')
            ],

            'est': [
                main.tr('spaCy - Estonian Word Tokenizer')
            ],

            'fin': [
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Finnish Word Tokenizer')
            ],

            'fra': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - French Word Tokenizer')
            ],

            'deu': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - German Word Tokenizer'),
                main.tr('syntok - Word Tokenizer')
            ],

            'ell': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Greek (Modern) Word Tokenizer')
            ],

            'guj': [
                main.tr('spaCy - Gujarati Word Tokenizer')
            ],

            'heb': [
                main.tr('spaCy - Hebrew Word Tokenizer')
            ],

            'hin': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Hindi Word Tokenizer')
            ],

            'hun': [
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Hungarian Word Tokenizer')
            ],

            'isl': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Icelandic Word Tokenizer'),
                main.tr('Tokenizer - Icelandic Word Tokenizer')
            ],

            'ind': [
                main.tr('spaCy - Indonesian Word Tokenizer')
            ],

            'gle': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Irish Word Tokenizer')
            ],

            'ita': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Italian Word Tokenizer')
            ],

            'jpn': [
                main.tr('nagisa - Japanese Word Tokenizer'),
                main.tr('Wordless - Japanese Kanji Tokenizer')
            ],

            'kan': [
                main.tr('spaCy - Kannada Word Tokenizer')
            ],

            'lav': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Latvian Word Tokenizer')
            ],

            'lij': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Ligurian Word Tokenizer')
            ],

            'lit': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Lithuanian Word Tokenizer')
            ],

            'ltz': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Luxembourgish Word Tokenizer')
            ],

            'mal': [
                main.tr('spaCy - Malayalam Word Tokenizer')
            ],

            'mar': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Marathi Word Tokenizer')
            ],

            'nep': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Nepali Word Tokenizer')
            ],

            'nob': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Norwegian Bokmål Word Tokenizer')
            ],

            'fas': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Persian Word Tokenizer')
            ],

            'pol': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Polish Word Tokenizer')
            ],

            'por': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Portuguese Word Tokenizer')
            ],

            'ron': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Romanian Word Tokenizer')
            ],

            'rus': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('razdel - Russian Word Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Russian Word Tokenizer')
            ],

            'srp_cyrl': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Serbian Word Tokenizer')
            ],

            'srp_latn': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Serbian Word Tokenizer')
            ],

            'sin': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Sinhala Word Tokenizer')
            ],

            'slk': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Slovak Word Tokenizer')
            ],

            'slv': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Slovenian Word Tokenizer')
            ],

            'spa': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Spanish Word Tokenizer'),
                main.tr('syntok - Word Tokenizer')
            ],

            'swe': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Swedish Word Tokenizer')
            ],

            'tgl': [
                main.tr('spaCy - Tagalog Word Tokenizer')
            ],

            'tgk': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
            ],

            'tam': [
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - Tamil Word Tokenizer')
            ],

            'tat': [
                main.tr('spaCy - Tatar Word Tokenizer')
            ],

            'tel': [
                main.tr('spaCy - Telugu Word Tokenizer')
            ],

            'tha': [
                main.tr('AttaCut - Thai Word Tokenizer'),
                main.tr('PyThaiNLP - Longest Matching'),
                main.tr('PyThaiNLP - Maximum Matching'),
                main.tr('PyThaiNLP - Maximum Matching + TCC'),
                main.tr('PyThaiNLP - Maximum Matching + TCC (Safe Mode)')
            ],

            'bod': [
                main.tr('botok - Tibetan Word Tokenizer')
            ],

            'tur': [
                main.tr('spaCy - Turkish Word Tokenizer')
            ],

            'ukr': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Ukrainian Word Tokenizer')
            ],

            'urd': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('spaCy - Urdu Word Tokenizer')
            ],

            'vie': [
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('Underthesea - Vietnamese Word Tokenizer')
            ],

            'yor': [
                main.tr('spaCy - Yoruba Word Tokenizer')
            ],

            'other': [
                main.tr('NLTK - NIST Tokenizer'),
                main.tr('NLTK - NLTK Tokenizer'),
                main.tr('NLTK - Penn Treebank Tokenizer'),
                main.tr('NLTK - Tok-tok Tokenizer'),
                main.tr('NLTK - Twitter Tokenizer'),
                main.tr('Sacremoses - Moses Tokenizer'),
                main.tr('spaCy - English Word Tokenizer'),
                main.tr('syntok - Word Tokenizer')
            ]
        },

        'word_detokenizers': {
            'cat': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'zho_cn': [
                main.tr('Wordless - Chinese Word Detokenizer')
            ],

            'zho_tw': [
                main.tr('Wordless - Chinese Word Detokenizer')
            ],

            'ces': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'nld': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'eng': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'fin': [
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'fra': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'deu': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'ell': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'hun': [
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'isl': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'gle': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'ita': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'jpn': [
                main.tr('Wordless - Japanese Word Detokenizer')
            ],

            'lav': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'lit': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'pol': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'por': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'ron': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'rus': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'slk': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'slv': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'spa': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'swe': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'tam': [
                main.tr('Sacremoses - Moses Detokenizer')
            ],

            'tha': [
                main.tr('Wordless - Thai Word Detokenizer')
            ],

            'bod': [
                main.tr('Wordless - Tibetan Word Detokenizer')
            ],

            'other': [
                main.tr('NLTK - Penn Treebank Detokenizer'),
                main.tr('Sacremoses - Moses Detokenizer')
            ]
        },

        'pos_taggers': {
            'zho_cn': [
                main.tr('jieba - Chinese POS Tagger')
            ],

            'zho_tw': [
                main.tr('jieba - Chinese POS Tagger')
            ],

            'dan': [
                main.tr('spaCy - Danish POS Tagger'),
            ],

            'nld': [
                main.tr('spaCy - Dutch POS Tagger')
            ],

            'eng': [
                main.tr('NLTK - Perceptron POS Tagger'),
                main.tr('spaCy - English POS Tagger')
            ],

            'fra': [
                main.tr('spaCy - French POS Tagger')
            ],

            'deu': [
                main.tr('spaCy - German POS Tagger')
            ],

            'ell': [
                main.tr('spaCy - Greek (Modern) POS Tagger')
            ],

            'ita': [
                main.tr('spaCy - Italian POS Tagger')
            ],

            'jpn': [
                main.tr('nagisa - Japanese POS Tagger')
            ],

            'lit': [
                main.tr('spaCy - Lithuanian POS Tagger')
            ],

            'nob': [
                main.tr('spaCy - Norwegian Bokmål POS Tagger')
            ],

            'pol': [
                main.tr('spaCy - Polish POS Tagger'),
            ],

            'por': [
                main.tr('spaCy - Portuguese POS Tagger')
            ],

            'ron': [
                main.tr('spaCy - Romanian POS Tagger')
            ],

            'rus': [
                main.tr('NLTK - Perceptron POS Tagger'),
                main.tr('pymorphy2 - Morphological Analyzer')
            ],

            'spa': [
                main.tr('spaCy - Spanish POS Tagger'),
            ],

            'tha': [
                main.tr('PyThaiNLP - Perceptron Tagger (ORCHID)'),
                main.tr('PyThaiNLP - Perceptron Tagger (PUD)')
            ],

            'bod': [
                main.tr('botok - Tibetan POS Tagger')
            ],

            'ukr': [
                main.tr('pymorphy2 - Morphological Analyzer')
            ],

            'vie': [
                main.tr('Underthesea - Vietnamese POS Tagger')
            ]
        },

        'lemmatizers': {
            'ast': [
                main.tr('Lemmatization Lists - Asturian Lemma List')
            ],

            'bul': [
                main.tr('Lemmatization Lists - Bulgarian Lemma List')
            ],

            'cat': [
                main.tr('Lemmatization Lists - Catalan Lemma List')
            ],

            'ces': [
                main.tr('Lemmatization Lists - Czech Lemma List')
            ],

            'dan': [
                main.tr('spaCy - Danish Lemmatizer')
            ],

            'nld': [
                main.tr('spaCy - Dutch Lemmatizer')
            ],

            'eng': [
                main.tr('Lemmatization Lists - English Lemma List'),
                main.tr('NLTK - WordNet Lemmatizer'),
                main.tr('spaCy - English Lemmatizer')
            ],

            'est': [
                main.tr('Lemmatization Lists - Estonian Lemma List')
            ],

            'fra': [
                main.tr('Lemmatization Lists - French Lemma List'),
                main.tr('spaCy - French Lemmatizer')
            ],

            'glg': [
                main.tr('Lemmatization Lists - Galician Lemma List')
            ],

            'deu': [
                main.tr('Lemmatization Lists - German Lemma List'),
                main.tr('spaCy - German Lemmatizer')
            ],

            'grc': [
                main.tr('lemmalist-greek - Greek (Ancient) Lemma List')
            ],

            'ell': [
                main.tr('spaCy - Greek (Modern) Lemmatizer')
            ],

            'hun': [
                main.tr('Lemmatization Lists - Hungarian Lemma List')
            ],

            'gle': [
                main.tr('Lemmatization Lists - Irish Lemma List')
            ],

            'ita': [
                main.tr('Lemmatization Lists - Italian Lemma List'),
                main.tr('spaCy - Italian Lemmatizer')
            ],

            'lit': [
                main.tr('spaCy - Lithuanian Lemmatizer')
            ],

            'glv': [
                main.tr('Lemmatization Lists - Manx Lemma List')
            ],

            'nob': [
                main.tr('spaCy - Norwegian Bokmål Lemmatizer')
            ],

            'fas': [
                main.tr('Lemmatization Lists - Persian Lemma List')
            ],

            'pol': [
                main.tr('spaCy - Polish Lemmatizer')
            ],

            'por': [
                main.tr('Lemmatization Lists - Portuguese Lemma List'),
                main.tr('spaCy - Portuguese Lemmatizer')
            ],

            'ron': [
                main.tr('Lemmatization Lists - Romanian Lemma List'),
                main.tr('spaCy - Romanian Lemmatizer')
            ],

            'rus': [
                main.tr('pymorphy2 - Morphological Analyzer')
            ],

            'gla': [
                main.tr('Lemmatization Lists - Scottish Gaelic Lemma List')
            ],

            'slk': [
                main.tr('Lemmatization Lists - Slovak Lemma List')
            ],

            'slv': [
                main.tr('Lemmatization Lists - Slovenian Lemma List')
            ],

            'spa': [
                main.tr('Lemmatization Lists - Spanish Lemma List'),
                main.tr('spaCy - Spanish Lemmatizer')
            ],

            'swe': [
                main.tr('Lemmatization Lists - Swedish Lemma List')
            ],

            'bod': [
                main.tr('botok - Tibetan Lemmatizer')
            ],

            'ukr': [
                main.tr('Lemmatization Lists - Ukrainian Lemma List'),
                main.tr('pymorphy2 - Morphological Analyzer')
            ],

            'cym': [
                main.tr('Lemmatization Lists - Welsh Lemma List')
            ]
        },

        'stop_word_lists': {
            'afr': [
                main.tr('spaCy - Afrikaans Stop Word List'),
                main.tr('Stopwords ISO - Afrikaans Stop Word List'),
                main.tr('Custom List')
            ],

            'sqi': [
                main.tr('extra-stopwords - Albanian Stop Word List'),
                main.tr('spaCy - Albanian Stop Word List'),
                main.tr('Custom List')
            ],

            'ara': [
                main.tr('extra-stopwords - Arabic Stop Word List'),
                main.tr('NLTK - Arabic Stop Word List'),
                main.tr('spaCy - Arabic Stop Word List'),
                main.tr('Stopwords ISO - Arabic Stop Word List'),
                main.tr('Custom List')
            ],

            'hye': [
                main.tr('extra-stopwords - Armenian Stop Word List'),
                main.tr('spaCy - Armenian Stop Word List'),
                main.tr('Stopwords ISO - Armenian Stop Word List'),
                main.tr('Custom List')
            ],

            'aze': [
                main.tr('NLTK - Azerbaijani Stop Word List'),
                main.tr('Custom List')
            ],

            'eus': [
                main.tr('extra-stopwords - Basque Stop Word List'),
                main.tr('spaCy - Basque Stop Word List'),
                main.tr('Stopwords ISO - Basque Stop Word List'),
                main.tr('Custom List')
            ],

            'bel': [
                main.tr('extra-stopwords - Belarusian Stop Word List'),
                main.tr('Custom List')
            ],

            'ben': [
                main.tr('extra-stopwords - Bengali Stop Word List'),
                main.tr('spaCy - Bengali Stop Word List'),
                main.tr('Stopwords ISO - Bengali Stop Word List'),
                main.tr('Custom List')
            ],

            'bre': [
                main.tr('Stopwords ISO - Breton Stop Word List'),
                main.tr('Custom List')
            ],

            'bul': [
                main.tr('extra-stopwords - Bulgarian Stop Word List'),
                main.tr('spaCy - Bulgarian Stop Word List'),
                main.tr('Stopwords ISO - Bulgarian Stop Word List'),
                main.tr('Custom List')
            ],

            'cat': [
                main.tr('extra-stopwords - Catalan Stop Word List'),
                main.tr('spaCy - Catalan Stop Word List'),
                main.tr('Stopwords ISO - Catalan Stop Word List'),
                main.tr('Custom List')
            ],

            'zho_cn': [
                main.tr('extra-stopwords - Chinese (Simplified) Stop Word List'),
                main.tr('spaCy - Chinese (Simplified) Stop Word List'),
                main.tr('Stopwords ISO - Chinese (Simplified) Stop Word List'),
                main.tr('Custom List')
            ],

            'zho_tw': [
                main.tr('extra-stopwords - Chinese (Traditional) Stop Word List'),
                main.tr('spaCy - Chinese (Traditional) Stop Word List'),
                main.tr('Stopwords ISO - Chinese (Traditional) Stop Word List'),
                main.tr('Custom List')
            ],

            'hrv': [
                main.tr('extra-stopwords - Croatian Stop Word List'),
                main.tr('spaCy - Croatian Stop Word List'),
                main.tr('Stopwords ISO - Croatian Stop Word List'),
                main.tr('Custom List')
            ],

            'ces': [
                main.tr('extra-stopwords - Czech Stop Word List'),
                main.tr('spaCy - Czech Stop Word List'),
                main.tr('Stopwords ISO - Czech Stop Word List'),
                main.tr('Custom List')
            ],

            'dan': [
                main.tr('extra-stopwords - Danish Stop Word List'),
                main.tr('NLTK - Danish Stop Word List'),
                main.tr('spaCy - Danish Stop Word List'),
                main.tr('Stopwords ISO - Danish Stop Word List'),
                main.tr('Custom List')
            ],

            'nld': [
                main.tr('extra-stopwords - Dutch Stop Word List'),
                main.tr('NLTK - Dutch Stop Word List'),
                main.tr('spaCy - Dutch Stop Word List'),
                main.tr('Stopwords ISO - Dutch Stop Word List'),
                main.tr('Custom List')
            ],

            'eng': [
                main.tr('extra-stopwords - English Stop Word List'),
                main.tr('NLTK - English Stop Word List'),
                main.tr('spaCy - English Stop Word List'),
                main.tr('Stopwords ISO - English Stop Word List'),
                main.tr('Custom List')
            ],

            'epo': [
                main.tr('Stopwords ISO - Esperanto Stop Word List'),
                main.tr('Custom List')
            ],

            'est': [
                main.tr('extra-stopwords - Estonian Stop Word List'),
                main.tr('spaCy - Estonian Stop Word List'),
                main.tr('Stopwords ISO - Estonian Stop Word List'),
                main.tr('Custom List')
            ],

            'fin': [
                main.tr('extra-stopwords - Finnish Stop Word List'),
                main.tr('NLTK - Finnish Stop Word List'),
                main.tr('spaCy - Finnish Stop Word List'),
                main.tr('Stopwords ISO - Finnish Stop Word List'),
                main.tr('Custom List')
            ],

            'fra': [
                main.tr('extra-stopwords - French Stop Word List'),
                main.tr('NLTK - French Stop Word List'),
                main.tr('spaCy - French Stop Word List'),
                main.tr('Stopwords ISO - French Stop Word List'),
                main.tr('Custom List')
            ],

            'glg': [
                main.tr('extra-stopwords - Galician Stop Word List'),
                main.tr('Stopwords ISO - Galician Stop Word List'),
                main.tr('Custom List')
            ],

            'deu': [
                main.tr('extra-stopwords - German Stop Word List'),
                main.tr('NLTK - German Stop Word List'),
                main.tr('spaCy - German Stop Word List'),
                main.tr('Stopwords ISO - German Stop Word List'),
                main.tr('Custom List')
            ],

            'grc': [
                main.tr('Stopwords ISO - Greek Stop Word List'),
                main.tr('Custom List')
            ],

            'ell': [
                main.tr('extra-stopwords - Greek (Modern) Stop Word List'),
                main.tr('NLTK - Greek (Modern) Stop Word List'),
                main.tr('spaCy - Greek (Modern) Stop Word List'),
                main.tr('Stopwords ISO - Greek Stop Word List'),
                main.tr('Custom List')
            ],

            'guj': [
                main.tr('spaCy - Gujarati Stop Word List'),
                main.tr('Stopwords ISO - Gujarati Stop Word List'),
                main.tr('Custom List')
            ],

            'hau': [
                main.tr('extra-stopwords - Hausa Stop Word List'),
                main.tr('Stopwords ISO - Hausa Stop Word List'),
                main.tr('Custom List')
            ],

            'heb': [
                main.tr('extra-stopwords - Hebrew Stop Word List'),
                main.tr('spaCy - Hebrew Stop Word List'),
                main.tr('Stopwords ISO - Hebrew Stop Word List'),
                main.tr('Custom List')
            ],

            'hin': [
                main.tr('extra-stopwords - Hindi Stop Word List'),
                main.tr('spaCy - Hindi Stop Word List'),
                main.tr('Stopwords ISO - Hindi Stop Word List'),
                main.tr('Custom List')
            ],

            'hun': [
                main.tr('extra-stopwords - Hungarian Stop Word List'),
                main.tr('NLTK - Hungarian Stop Word List'),
                main.tr('spaCy - Hungarian Stop Word List'),
                main.tr('Stopwords ISO - Hungarian Stop Word List'),
                main.tr('Custom List')
            ],

            'isl': [
                main.tr('extra-stopwords - Icelandic Stop Word List'),
                main.tr('spaCy - Icelandic Stop Word List'),
                main.tr('Custom List')
            ],

            'ind': [
                main.tr('extra-stopwords - Indonesian Stop Word List'),
                main.tr('NLTK - Indonesian Stop Word List'),
                main.tr('spaCy - Indonesian Stop Word List'),
                main.tr('Stopwords ISO - Indonesian Stop Word List'),
                main.tr('Custom List')
            ],

            'gle': [
                main.tr('extra-stopwords - Irish Stop Word List'),
                main.tr('spaCy - Irish Stop Word List'),
                main.tr('Stopwords ISO - Irish Stop Word List'),
                main.tr('Custom List')
            ],

            'ita': [
                main.tr('extra-stopwords - Italian Stop Word List'),
                main.tr('NLTK - Italian Stop Word List'),
                main.tr('spaCy - Italian Stop Word List'),
                main.tr('Stopwords ISO - Italian Stop Word List'),
                main.tr('Custom List')
            ],

            'jpn': [
                main.tr('extra-stopwords - Japanese Stop Word List'),
                main.tr('spaCy - Japanese Stop Word List'),
                main.tr('Stopwords ISO - Japanese Stop Word List'),
                main.tr('Custom List')
            ],

            'kan': [
                main.tr('spaCy - Kannada Stop Word List'),
                main.tr('Custom List')
            ],

            'kaz': [
                main.tr('NLTK - Kazakh Stop Word List'),
                main.tr('Custom List')
            ],

            'kor': [
                main.tr('extra-stopwords - Korean Stop Word List'),
                main.tr('Stopwords ISO - Korean Stop Word List'),
                main.tr('Custom List')
            ],

            'kur': [
                main.tr('extra-stopwords - Kurdish Stop Word List'),
                main.tr('Stopwords ISO - Kurdish Stop Word List'),
                main.tr('Custom List')
            ],

            'lat': [
                main.tr('Stopwords ISO - Latin Stop Word List'),
                main.tr('Custom List')
            ],

            'lav': [
                main.tr('extra-stopwords - Latvian Stop Word List'),
                main.tr('spaCy - Latvian Stop Word List'),
                main.tr('Stopwords ISO - Latvian Stop Word List'),
                main.tr('Custom List')
            ],

            'lij': [
                main.tr('spaCy - Ligurian Stop Word List'),
                main.tr('Custom List')
            ],

            'lit': [
                main.tr('extra-stopwords - Lithuanian Stop Word List'),
                main.tr('spaCy - Lithuanian Stop Word List'),
                main.tr('Stopwords ISO - Lithuanian Stop Word List'),
                main.tr('Custom List')
            ],

            'ltz': [
                main.tr('spaCy - Luxembourgish Stop Word List'),
                main.tr('Custom List')
            ],

            'msa': [
                main.tr('extra-stopwords - Malay Stop Word List'),
                main.tr('Stopwords ISO - Malay Stop Word List'),
                main.tr('Custom List')
            ],

            'mal': [
                main.tr('spaCy - Malayalam Stop Word List'),
                main.tr('Custom List')
            ],

            'mar': [
                main.tr('extra-stopwords - Marathi Stop Word List'),
                main.tr('spaCy - Marathi Stop Word List'),
                main.tr('Stopwords ISO - Marathi Stop Word List'),
                main.tr('Custom List')
            ],

            'mon': [
                main.tr('extra-stopwords - Mongolian Stop Word List'),
                main.tr('Custom List')
            ],

            'nep': [
                main.tr('extra-stopwords - Nepali Stop Word List'),
                main.tr('NLTK - Nepali Stop Word List'),
                main.tr('spaCy - Nepali Stop Word List'),
                main.tr('Custom List')
            ],

            'nob': [
                main.tr('extra-stopwords - Norwegian Bokmål Stop Word List'),
                main.tr('NLTK - Norwegian Bokmål Stop Word List'),
                main.tr('spaCy - Norwegian Bokmål Stop Word List'),
                main.tr('Stopwords ISO - Norwegian Stop Word List'),
                main.tr('Custom List')
            ],

            'nno': [
                main.tr('extra-stopwords - Norwegian Bokmål Stop Word List'),
                main.tr('NLTK - Norwegian Nynorsk Stop Word List'),
                main.tr('Stopwords ISO - Norwegian Stop Word List'),
                main.tr('Custom List')
            ],

            'fas': [
                main.tr('extra-stopwords - Persian Stop Word List'),
                main.tr('spaCy - Persian Stop Word List'),
                main.tr('Stopwords ISO - Persian Stop Word List'),
                main.tr('Custom List')
            ],

            'pol': [
                main.tr('extra-stopwords - Polish Stop Word List'),
                main.tr('spaCy - Polish Stop Word List'),
                main.tr('Stopwords ISO - Polish Stop Word List'),
                main.tr('Custom List')
            ],

            'por': [
                main.tr('extra-stopwords - Portuguese Stop Word List'),
                main.tr('NLTK - Portuguese Stop Word List'),
                main.tr('spaCy - Portuguese Stop Word List'),
                main.tr('Stopwords ISO - Portuguese Stop Word List'),
                main.tr('Custom List')
            ],

            'ron': [
                main.tr('extra-stopwords - Romanian Stop Word List'),
                main.tr('NLTK - Romanian Stop Word List'),
                main.tr('spaCy - Romanian Stop Word List'),
                main.tr('Stopwords ISO - Romanian Stop Word List'),
                main.tr('Custom List')
            ],

            'rus': [
                main.tr('extra-stopwords - Russian Stop Word List'),
                main.tr('NLTK - Russian Stop Word List'),
                main.tr('spaCy - Russian Stop Word List'),
                main.tr('Stopwords ISO - Russian Stop Word List'),
                main.tr('Custom List')
            ],

            'srp_cyrl': [
                main.tr('extra-stopwords - Serbian (Cyrillic) Stop Word List'),
                main.tr('spaCy - Serbian (Cyrillic) Stop Word List'),
                main.tr('Custom List')
            ],

            'srp_latn': [
                main.tr('extra-stopwords - Serbian (Latin) Stop Word List'),
                main.tr('spaCy - Serbian (Latin) Stop Word List'),
                main.tr('Custom List')
            ],

            'sin': [
                main.tr('spaCy - Sinhala Stop Word List'),
                main.tr('Custom List')
            ],

            'slk': [
                main.tr('extra-stopwords - Slovak Stop Word List'),
                main.tr('spaCy - Slovak Stop Word List'),
                main.tr('Stopwords ISO - Slovak Stop Word List'),
                main.tr('Custom List')
            ],

            'slv': [
                main.tr('extra-stopwords - Slovenian Stop Word List'),
                main.tr('NLTK - Slovenian Stop Word List'),
                main.tr('spaCy - Slovenian Stop Word List'),
                main.tr('Stopwords ISO - Slovenian Stop Word List'),
                main.tr('Custom List')
            ],

            'som': [
                main.tr('Stopwords ISO - Somali Stop Word List'),
                main.tr('Custom List')
            ],

            'sot': [
                main.tr('Stopwords ISO - Sotho (Southern) Stop Word List'),
                main.tr('Custom List')
            ],

            'spa': [
                main.tr('extra-stopwords - Spanish Stop Word List'),
                main.tr('NLTK - Spanish Stop Word List'),
                main.tr('spaCy - Spanish Stop Word List'),
                main.tr('Stopwords ISO - Spanish Stop Word List'),
                main.tr('Custom List')
            ],

            'swa': [
                main.tr('extra-stopwords - Swahili Stop Word List'),
                main.tr('Stopwords ISO - Swahili Stop Word List'),
                main.tr('Custom List')
            ],

            'swe': [
                main.tr('extra-stopwords - Swedish Stop Word List'),
                main.tr('NLTK - Swedish Stop Word List'),
                main.tr('spaCy - Swedish Stop Word List'),
                main.tr('Stopwords ISO - Swedish Stop Word List'),
                main.tr('Custom List')
            ],

            'tgl': [
                main.tr('extra-stopwords - Tagalog Stop Word List'),
                main.tr('spaCy - Tagalog Stop Word List'),
                main.tr('Stopwords ISO - Tagalog Stop Word List'),
                main.tr('Custom List')
            ],

            'tgk': [
                main.tr('NLTK - Tajik Stop Word List'),
                main.tr('Custom List')
            ],

            'tam': [
                main.tr('spaCy - Tamil Stop Word List'),
                main.tr('Custom List')
            ],

            'tat': [
                main.tr('spaCy - Tatar Stop Word List'),
                main.tr('Custom List')
            ],

            'tel': [
                main.tr('extra-stopwords - Telugu Stop Word List'),
                main.tr('spaCy - Telugu Stop Word List'),
                main.tr('Custom List')
            ],

            'tha': [
                main.tr('extra-stopwords - Thai Stop Word List'),
                main.tr('PyThaiNLP - Thai Stop Word List'),
                main.tr('spaCy - Thai Stop Word List'),
                main.tr('Stopwords ISO - Thai Stop Word List'),
                main.tr('Custom List')
            ],

            'tur': [
                main.tr('extra-stopwords - Turkish Stop Word List'),
                main.tr('NLTK - Turkish Stop Word List'),
                main.tr('spaCy - Turkish Stop Word List'),
                main.tr('Stopwords ISO - Turkish Stop Word List'),
                main.tr('Custom List')
            ],

            'ukr': [
                main.tr('extra-stopwords - Ukrainian Stop Word List'),
                main.tr('spaCy - Ukrainian Stop Word List'),
                main.tr('Stopwords ISO - Ukrainian Stop Word List'),
                main.tr('Custom List')
            ],

            'urd': [
                main.tr('extra-stopwords - Urdu Stop Word List'),
                main.tr('spaCy - Urdu Stop Word List'),
                main.tr('Stopwords ISO - Urdu Stop Word List'),
                main.tr('Custom List')
            ],

            'vie': [
                main.tr('extra-stopwords - Vietnamese Stop Word List'),
                main.tr('spaCy - Vietnamese Stop Word List'),
                main.tr('Stopwords ISO - Vietnamese Stop Word List'),
                main.tr('Custom List')
            ],

            'yor': [
                main.tr('extra-stopwords - Yoruba Stop Word List'),
                main.tr('spaCy - Yoruba Stop Word List'),
                main.tr('Stopwords ISO - Yoruba Stop Word List'),
                main.tr('Custom List')
            ],

            'zul': [
                main.tr('Stopwords ISO - Zulu Stop Word List'),
                main.tr('Custom List')
            ],

            'other': [
                main.tr('Custom List')
            ]
        },

        'measures_dispersion': {
            main.tr('Juilland’s D'): {
                'col': main.tr('Juilland\'s D'),
                'func': wl_measures_dispersion.juillands_d
            },

            main.tr('Carroll’s D₂'): {
                'col': main.tr('Carroll\'s D₂'),
                'func': wl_measures_dispersion.carrolls_d2
            },

            main.tr('Lyne’s D₃'): {
                'col': main.tr('Lyne\'s D₃'),
                'func': wl_measures_dispersion.lynes_d3
            },

            main.tr('Rosengren’s S'): {
                'col': main.tr('Rosengren\'s S'),
                'func': wl_measures_dispersion.rosengrens_s
            },

            main.tr('Zhang’s Distributional Consistency'): {
                'col': main.tr('Zhang\'s DC'),
                'func': wl_measures_dispersion.zhangs_distributional_consistency
            },

            main.tr('Gries’s DP'): {
                'col': main.tr('Gries\'s DP'),
                'func': wl_measures_dispersion.griess_dp
            },

            main.tr('Gries’s DPnorm'): {
                'col': main.tr('Gries\'s DPnorm'),
                'func': wl_measures_dispersion.griess_dp_norm
            }
        },

        'measures_adjusted_freq': {
            main.tr('Juilland’s U'): {
                'col': main.tr('Juilland\'s U'),
                'func': wl_measures_adjusted_freq.juillands_u
            },

            main.tr('Carroll’s Um'): {
                'col': main.tr('Carroll\'s Um'),
                'func': wl_measures_adjusted_freq.carrolls_um
            },

            main.tr('Rosengren’s KF'): {
                'col': main.tr('Rosengren\'s KF'),
                'func': wl_measures_adjusted_freq.rosengrens_kf
            },

            main.tr('Engwall’s FM'): {
                'col': main.tr('Engwall\'s FM'),
                'func': wl_measures_adjusted_freq.engwalls_fm
            },

            main.tr('Kromer’s UR'): {
                'col': main.tr('Kromer\'s UR'),
                'func': wl_measures_adjusted_freq.kromers_ur
            }
        },

        'tests_significance': {
            'collocation': {
                main.tr('z-score'): {
                    'cols': [
                        main.tr('z-score'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.z_score
                },

                main.tr('Berry-Rogghe’s z-score'): {
                    'cols': [
                        main.tr('Berry-Rogghe’s z-score'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.berry_rogghes_z_score
                },

                main.tr('Student’s t-test (One-sample)'): {
                    'cols': [
                        main.tr('t-statistic'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.students_t_test_1_sample
                },

                main.tr('Pearson’s Chi-squared Test'): {
                    'cols': [
                        main.tr('χ2'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.pearsons_chi_squared_test
                },

                main.tr('Log-likelihood Ratio Test'): {
                    'cols': [
                        main.tr('Log-likelihood Ratio'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.log_likehood_ratio_test
                },

                main.tr('Fisher’s Exact Test'): {
                    'cols': [
                        None,
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.fishers_exact_test
                }
            },

            'keyword': {
                main.tr('Student’s t-test (Two-sample)'): {
                    'cols': [
                        main.tr('t-statistic'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.students_t_test_2_sample
                },

                main.tr('Pearson’s Chi-squared Test'): {
                    'cols': [
                        main.tr('χ2'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.pearsons_chi_squared_test
                },


                main.tr('Fisher’s Exact Test'): {
                    'cols': [
                        None,
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.fishers_exact_test
                },

                main.tr('Log-likelihood Ratio Test'): {
                    'cols': [
                        main.tr('Log-likelihood Ratio'),
                        main.tr('p-value'),
                        main.tr('Bayes Factor')
                    ],

                    'func': wl_measures_statistical_significance.log_likehood_ratio_test
                },

                main.tr('Mann-Whitney U Test'): {
                    'cols': [
                        main.tr('U Statistic'),
                        main.tr('p-value'),
                        None
                    ],

                    'func': wl_measures_statistical_significance.mann_whitney_u_test
                }
            }
        },

        'measures_effect_size': {
            'collocation': {
                main.tr('Pointwise Mutual Information'): {
                    'col': main.tr('PMI'),
                    'func': wl_measures_effect_size.pmi
                },

                main.tr('Mutual Dependency'): {
                    'col': main.tr('MD'),
                    'func': wl_measures_effect_size.md
                },

                main.tr('Log-Frequency Biased MD'): {
                    'col': main.tr('LFMD'),
                    'func': wl_measures_effect_size.lfmd
                },

                main.tr('Cubic Association Ratio'): {
                    'col': main.tr('IM³'),
                    'func': wl_measures_effect_size.im3
                },

                main.tr('MI.log-f'): {
                    'col': main.tr('MI.log-f'),
                    'func': wl_measures_effect_size.mi_log_f
                },

                main.tr('Mutual Information'): {
                    'col': main.tr('MI'),
                    'func': wl_measures_effect_size.mi
                },

                main.tr('Squared Phi Coefficient'): {
                    'col': main.tr('φ2'),
                    'func': wl_measures_effect_size.squared_phi_coeff
                },

                main.tr('Dice’s Coefficient'): {
                    'col': main.tr('Dice’s Coefficient'),
                    'func': wl_measures_effect_size.dices_coeff
                },

                main.tr('logDice'): {
                    'col': main.tr('logDice'),
                    'func': wl_measures_effect_size.log_dice
                },

                main.tr('Mutual Expectation'): {
                    'col': main.tr('ME'),
                    'func': wl_measures_effect_size.me
                },

                main.tr('Jaccard Index'): {
                    'col': main.tr('Jaccard Index'),
                    'func': wl_measures_effect_size.jaccard_index
                },

                main.tr('Minimum Sensitivity'): {
                    'col': main.tr('Minimum Sensitivity'),
                    'func': wl_measures_effect_size.min_sensitivity
                },

                main.tr('Poisson Collocation Measure'): {
                    'col': main.tr('Poisson Collocation Measure'),
                    'func': wl_measures_effect_size.poisson_collocation_measure
                }
            },

            'keyword': {
                main.tr('Kilgarriff’s Ratio'): {
                    'col': main.tr('Kilgarriff’s Ratio'),
                    'func': wl_measures_effect_size.kilgarriffs_ratio
                },

                main.tr('Odds Ratio'): {
                    'col': main.tr('Odds Ratio'),
                    'func': wl_measures_effect_size.odds_ratio
                },

                main.tr('Log Ratio'): {
                    'col': main.tr('Log Ratio'),
                    'func': wl_measures_effect_size.log_ratio
                },

                main.tr('Difference Coefficient'): {
                    'col': main.tr('Difference Coefficient'),
                    'func': wl_measures_effect_size.diff_coeff
                },

                main.tr('%DIFF'): {
                    'col': main.tr('%DIFF'),
                    'func': wl_measures_effect_size.pct_diff
                }
            }
        },

        'styles': {
            'style_dialog': '''
                <head>
                    <style>
                        * {
                            outline: none;
                            margin: 0;
                            border: 0;
                            padding: 0;

                            line-height: 1.2;
                            text-align: justify;
                        }

                        div {
                            margin-bottom: 5px;
                        }

                        ul {
                            margin-bottom: 5px;
                        }

                        li {
                            margin-left: -30px;
                        }
                    </style>
                </head>
            ''',

            'style_changelog': f'''
                <head>
                    <style>
                        * {{
                            outline: none;
                            margin: 0;
                            border: 0;
                            padding: 0;

                            text-align: justify;
                        }}

                        ul {{
                            line-height: 1.2;
                            margin-bottom: 10px;
                        }}

                        li {{
                            margin-left: -30px;
                        }}

                        .changelog {{
                            margin-bottom: 5px;
                        }}

                        .changelog-header {{
                            margin-bottom: 3px;
                            font-size: {font_size_custom + 2}px;
                            font-weight: bold;
                        }}

                        .changelog-section-header {{
                            margin-bottom: 5px;
                            font-size: {font_size_custom + 1}px;
                            font-weight: bold;
                        }}
                    </style>
                </head>
            ''',

            'style_normal': '''
                color: #000
            ''',

            'style_important': '''
                color: #F00;
            ''',

            'style_hint': '''
                color: #777;
            '''
        }
    }
