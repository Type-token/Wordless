#
# Wordless: Overview
#
# Copyright (C) 2018-2021  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import collections
import copy
import itertools
import re
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy

from wl_checking import wl_checking_file
from wl_dialogs import wl_dialog_misc, wl_msg_box
from wl_text import wl_text, wl_text_utils, wl_token_processing
from wl_utils import wl_misc, wl_threading
from wl_widgets import wl_box, wl_layout, wl_msg, wl_table, wl_widgets

class Wl_Table_Overview(wl_table.Wl_Table_Data):
    def __init__(self, parent):
        super().__init__(
            parent,
            headers = [
                parent.tr('Count of Paragraphs'),
                parent.tr('Count of Paragraphs %'),
                parent.tr('Count of Sentences'),
                parent.tr('Count of Sentences %'),
                parent.tr('Count of Tokens'),
                parent.tr('Count of Tokens %'),
                parent.tr('Count of Types'),
                parent.tr('Count of Types %'),
                parent.tr('Count of Characters'),
                parent.tr('Count of Characters %'),
                parent.tr('Type-Token Ratio'),
                parent.tr('Type-Token Ratio (Standardized)'),
                parent.tr('Paragraph Length in Sentence (Mean)'),
                parent.tr('Paragraph Length in Sentence (Standard Deviation)'),
                parent.tr('Paragraph Length in Token (Mean)'),
                parent.tr('Paragraph Length in Token (Standard Deviation)'),
                parent.tr('Sentence Length in Token (Mean)'),
                parent.tr('Sentence Length in Token (Standard Deviation)'),
                parent.tr('Token Length in Character (Mean)'),
                parent.tr('Token Length in Character (Standard Deviation)'),
                parent.tr('Type Length in Character (Mean)'),
                parent.tr('Type Length in Character (Standard Deviation)')
            ],
            header_orientation = 'vertical',
            headers_int = [
                parent.tr('Count of Paragraphs'),
                parent.tr('Count of Sentences'),
                parent.tr('Count of Tokens'),
                parent.tr('Count of Types'),
                parent.tr('Count of Characters')
            ],
            headers_float = [
                parent.tr('Type-Token Ratio'),
                parent.tr('Type-Token Ratio (Standardized)'),
                parent.tr('Paragraph Length in Sentence (Mean)'),
                parent.tr('Paragraph Length in Sentence (Standard Deviation)'),
                parent.tr('Paragraph Length in Token (Mean)'),
                parent.tr('Paragraph Length in Token (Standard Deviation)'),
                parent.tr('Sentence Length in Token (Mean)'),
                parent.tr('Sentence Length in Token (Standard Deviation)'),
                parent.tr('Token Length in Character (Mean)'),
                parent.tr('Token Length in Character (Standard Deviation)'),
                parent.tr('Type Length in Character (Mean)'),
                parent.tr('Type Length in Character (Standard Deviation)')
            ],
            headers_pct = [
                parent.tr('Count of Paragraphs %'),
                parent.tr('Count of Sentences %'),
                parent.tr('Count of Tokens %'),
                parent.tr('Count of Types %'),
                parent.tr('Count of Characters %')
            ],
            headers_cumulative = [
                parent.tr('Count of Paragraphs'),
                parent.tr('Count of Paragraphs %'),
                parent.tr('Count of Sentences'),
                parent.tr('Count of Sentences %'),
                parent.tr('Count of Tokens'),
                parent.tr('Count of Tokens %'),
                parent.tr('Count of Types'),
                parent.tr('Count of Types %'),
                parent.tr('Count of Characters'),
                parent.tr('Count of Characters %')
            ]
        )
        
        self.name = 'overview'

        self.button_generate_table = QPushButton(self.tr('Generate Table'), self)

        self.button_generate_table.clicked.connect(lambda: generate_table(self.main, self))

    def clear_table(self, count_headers = 1):
        super().clear_table(0)

        self.insert_col(0, self.tr('Total'))

class Wrapper_Overview(wl_layout.Wl_Wrapper):
    def __init__(self, main):
        super().__init__(main)

        # Table
        self.table_overview = Wl_Table_Overview(self)

        self.wrapper_table.layout().addWidget(self.table_overview, 0, 0, 1, 4)
        self.wrapper_table.layout().addWidget(self.table_overview.button_generate_table, 1, 0)
        self.wrapper_table.layout().addWidget(self.table_overview.button_export_selected, 1, 1)
        self.wrapper_table.layout().addWidget(self.table_overview.button_export_all, 1, 2)
        self.wrapper_table.layout().addWidget(self.table_overview.button_clear, 1, 3)
        
        # Token Settings
        self.group_box_token_settings = QGroupBox(self.tr('Token Settings'), self)

        (self.checkbox_words,
         self.checkbox_lowercase,
         self.checkbox_uppercase,
         self.checkbox_title_case,
         self.checkbox_nums,
         self.checkbox_puncs,

         self.checkbox_treat_as_lowercase,
         self.checkbox_lemmatize_tokens,
         self.checkbox_filter_stop_words,

         self.checkbox_ignore_tags,
         self.checkbox_use_tags) = wl_widgets.wl_widgets_token_settings(self)

        self.checkbox_words.stateChanged.connect(self.token_settings_changed)
        self.checkbox_lowercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_uppercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_title_case.stateChanged.connect(self.token_settings_changed)
        self.checkbox_nums.stateChanged.connect(self.token_settings_changed)
        self.checkbox_puncs.stateChanged.connect(self.token_settings_changed)

        self.checkbox_treat_as_lowercase.stateChanged.connect(self.token_settings_changed)
        self.checkbox_lemmatize_tokens.stateChanged.connect(self.token_settings_changed)
        self.checkbox_filter_stop_words.stateChanged.connect(self.token_settings_changed)

        self.checkbox_ignore_tags.stateChanged.connect(self.token_settings_changed)
        self.checkbox_use_tags.stateChanged.connect(self.token_settings_changed)

        self.group_box_token_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_token_settings.layout().addWidget(self.checkbox_words, 0, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_lowercase, 0, 1)
        self.group_box_token_settings.layout().addWidget(self.checkbox_uppercase, 1, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_title_case, 1, 1)
        self.group_box_token_settings.layout().addWidget(self.checkbox_nums, 2, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_puncs, 2, 1)

        self.group_box_token_settings.layout().addWidget(wl_layout.Wl_Separator(self), 3, 0, 1, 2)

        self.group_box_token_settings.layout().addWidget(self.checkbox_treat_as_lowercase, 4, 0, 1, 2)
        self.group_box_token_settings.layout().addWidget(self.checkbox_lemmatize_tokens, 5, 0, 1, 2)
        self.group_box_token_settings.layout().addWidget(self.checkbox_filter_stop_words, 6, 0, 1, 2)

        self.group_box_token_settings.layout().addWidget(wl_layout.Wl_Separator(self), 7, 0, 1, 2)

        self.group_box_token_settings.layout().addWidget(self.checkbox_ignore_tags, 8, 0)
        self.group_box_token_settings.layout().addWidget(self.checkbox_use_tags, 8, 1)

        # Generation Settings
        self.group_box_generation_settings = QGroupBox(self.tr('Generation Settings'), self)

        self.label_base_sttr = QLabel(self.tr('Base of standardized type-token ratio:'), self)
        self.spin_box_base_sttr = wl_box.Wl_Spin_Box(self)

        self.spin_box_base_sttr.setRange(100, 10000)

        self.spin_box_base_sttr.valueChanged.connect(self.generation_settings_changed)

        self.group_box_generation_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_generation_settings.layout().addWidget(self.label_base_sttr, 0, 0)
        self.group_box_generation_settings.layout().addWidget(self.spin_box_base_sttr, 1, 0)

        # Table Settings
        self.group_box_table_settings = QGroupBox(self.tr('Table Settings'), self)

        (self.checkbox_show_pct,
         self.checkbox_show_cumulative,
         self.checkbox_show_breakdown) = wl_widgets.wl_widgets_table_settings(
            self,
            table = self.table_overview
        )

        self.checkbox_show_pct.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_cumulative.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_breakdown.stateChanged.connect(self.table_settings_changed)

        self.group_box_table_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_pct, 0, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_cumulative, 1, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_breakdown, 2, 0)

        self.wrapper_settings.layout().addWidget(self.group_box_token_settings, 0, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_generation_settings, 1, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_table_settings, 2, 0)

        self.wrapper_settings.layout().setRowStretch(3, 1)

        self.load_settings()

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.main.settings_default['overview'])
        else:
            settings = copy.deepcopy(self.main.settings_custom['overview'])

        # Token Settings
        self.checkbox_words.setChecked(settings['token_settings']['words'])
        self.checkbox_lowercase.setChecked(settings['token_settings']['lowercase'])
        self.checkbox_uppercase.setChecked(settings['token_settings']['uppercase'])
        self.checkbox_title_case.setChecked(settings['token_settings']['title_case'])
        self.checkbox_nums.setChecked(settings['token_settings']['nums'])
        self.checkbox_puncs.setChecked(settings['token_settings']['puncs'])

        self.checkbox_treat_as_lowercase.setChecked(settings['token_settings']['treat_as_lowercase'])
        self.checkbox_lemmatize_tokens.setChecked(settings['token_settings']['lemmatize_tokens'])
        self.checkbox_filter_stop_words.setChecked(settings['token_settings']['filter_stop_words'])

        self.checkbox_ignore_tags.setChecked(settings['token_settings']['ignore_tags'])
        self.checkbox_use_tags.setChecked(settings['token_settings']['use_tags'])

        # Generation Settings
        self.spin_box_base_sttr.setValue(settings['generation_settings']['base_sttr'])

        # Table Settings
        self.checkbox_show_pct.setChecked(settings['table_settings']['show_pct'])
        self.checkbox_show_cumulative.setChecked(settings['table_settings']['show_cumulative'])
        self.checkbox_show_breakdown.setChecked(settings['table_settings']['show_breakdown'])

        self.token_settings_changed()
        self.generation_settings_changed()
        self.table_settings_changed()

    def token_settings_changed(self):
        settings = self.main.settings_custom['overview']['token_settings']

        settings['words'] = self.checkbox_words.isChecked()
        settings['lowercase'] = self.checkbox_lowercase.isChecked()
        settings['uppercase'] = self.checkbox_uppercase.isChecked()
        settings['title_case'] = self.checkbox_title_case.isChecked()
        settings['nums'] = self.checkbox_nums.isChecked()
        settings['puncs'] = self.checkbox_puncs.isChecked()

        settings['treat_as_lowercase'] = self.checkbox_treat_as_lowercase.isChecked()
        settings['lemmatize_tokens'] = self.checkbox_lemmatize_tokens.isChecked()
        settings['filter_stop_words'] = self.checkbox_filter_stop_words.isChecked()

        settings['ignore_tags'] = self.checkbox_ignore_tags.isChecked()
        settings['use_tags'] = self.checkbox_use_tags.isChecked()

        if settings['use_tags']:
            self.label_base_sttr.setText(self.tr('Base of standardized type-tag ratio:'))
        else:
            self.label_base_sttr.setText(self.tr('Base of standardized type-token ratio:'))

    def generation_settings_changed(self):
        settings = self.main.settings_custom['overview']['generation_settings']

        settings['base_sttr'] = self.spin_box_base_sttr.value()

    def table_settings_changed(self):
        settings = self.main.settings_custom['overview']['table_settings']

        settings['show_pct'] = self.checkbox_show_pct.isChecked()
        settings['show_cumulative'] = self.checkbox_show_cumulative.isChecked()
        settings['show_breakdown'] = self.checkbox_show_breakdown.isChecked()

class Wl_Worker_Overview(wl_threading.Wl_Worker):
    worker_done = pyqtSignal(list)

    def __init__(self, main, dialog_progress, update_gui):
        super().__init__(main, dialog_progress, update_gui)

        self.texts_stats_files = []

    def run(self):
        texts = []

        settings = self.main.settings_custom['overview']
        files = self.main.wl_files.get_selected_files()

        for i, file in enumerate(files):
            text = wl_text.Wl_Text(self.main, file)
            text = wl_token_processing.wl_process_tokens_overview(
                text,
                token_settings = settings['token_settings']
            )

            texts.append(text)

        if len(files) > 1:
            text_total = wl_text.Wl_Text_Blank()
            text_total.offsets_paras = [
                offset
                for text in texts
                for offset in text.offsets_paras
            ]
            text_total.offsets_sentences = [
                offset
                for text in texts
                for offset in text.offsets_sentences
            ]
            text_total.tokens_multilevel = [
                para
                for text in texts
                for para in text.tokens_multilevel
            ]
            text_total.tokens_flat = [
                token
                for text in texts
                for token in text.tokens_flat
            ]

            texts.append(text_total)
        else:
            texts.append(texts[0])

        self.progress_updated.emit(self.tr('Processing data ...'))

        base_sttr = settings['generation_settings']['base_sttr']

        for text in texts:
            texts_stats_file = []

            # Paragraph length
            len_paras_in_sentence = [len(para) for para in text.tokens_multilevel]
            len_paras_in_token = [
                sum([len(sentence) for sentence in para])
                for para in text.tokens_multilevel
            ]

            # Sentence length
            len_sentences = [
                len(sentence)
                for para in text.tokens_multilevel
                for sentence in para
            ]

            # Token length
            len_tokens = [len(token) for token in text.tokens_flat]
            # Type length
            len_types = [len(token_type) for token_type in set(text.tokens_flat)]

            count_tokens = len(len_tokens)
            count_types = len(len_types)

            # TTR
            if count_tokens:
                ttr = count_types / count_tokens
            else:
                ttr = 0

            # STTR
            if count_tokens < base_sttr:
                sttr = ttr
            else:
                token_sections = wl_text_utils.to_sections_unequal(text.tokens_flat, base_sttr)

                # Discard the last section if number of tokens in it is smaller than the base of sttr
                if len(token_sections[-1]) < base_sttr:
                    ttrs = [
                        len(set(token_section)) / len(token_section)
                        for token_section in token_sections[:-1]
                    ]
                else:
                    ttrs = [
                        len(set(token_section)) / len(token_section)
                        for token_section in token_sections
                    ]

                sttr = sum(ttrs) / len(ttrs)

            texts_stats_file.append(len_paras_in_sentence)
            texts_stats_file.append(len_paras_in_token)
            texts_stats_file.append(len_sentences)
            texts_stats_file.append(len_tokens)
            texts_stats_file.append(len_types)
            texts_stats_file.append(ttr)
            texts_stats_file.append(sttr)

            self.texts_stats_files.append(texts_stats_file)

class Wl_Worker_Overview_Table(Wl_Worker_Overview):
    def run(self):
        super().run()

        self.progress_updated.emit(self.tr('Rendering table ...'))

        time.sleep(0.1)

        self.worker_done.emit(self.texts_stats_files)

@wl_misc.log_timing
def generate_table(main, table):
    def update_gui(texts_stats_files):
        if any(itertools.chain.from_iterable(texts_stats_files)):
            table.settings = copy.deepcopy(main.settings_custom)

            table.blockSignals(True)
            table.setUpdatesEnabled(False)

            table.clear_table()

            count_tokens_lens = []
            count_sentences_lens = []

            # Insert column (total)
            for i, file in enumerate(files):
                table.insert_col(table.find_col(main.tr('Total')), file['name'],
                                 is_breakdown = True)

            count_paras_total = len(texts_stats_files[-1][0])
            count_sentences_total = len(texts_stats_files[-1][2])
            count_tokens_total = len(texts_stats_files[-1][3])
            count_types_total = len(texts_stats_files[-1][4])
            count_chars_total = sum(texts_stats_files[-1][3])

            for i, stats in enumerate(texts_stats_files):
                len_paras_in_sentence = stats[0]
                len_paras_in_token = stats[1]
                len_sentences = stats[2]
                len_tokens = stats[3]
                len_types = stats[4]
                ttr = stats[5]
                sttr = stats[6]

                count_paras = len(len_paras_in_sentence)
                count_sentences = len(len_sentences)
                count_tokens = len(len_tokens)
                count_types = len(len_types)
                count_chars = sum(len_tokens)

                # Count of Paragraphs
                table.set_item_num(0, i, count_paras)
                table.set_item_num(1, i, count_paras, count_paras_total)
                # Count of Sentences
                table.set_item_num(2, i, count_sentences)
                table.set_item_num(3, i, count_sentences, count_sentences_total)
                # Count of Tokens
                table.set_item_num(4, i, count_tokens)
                table.set_item_num(5, i, count_tokens, count_tokens_total)
                # Count of Types
                table.set_item_num(6, i, count_types)
                table.set_item_num(7, i, count_types, count_types_total)
                # Count of Characters
                table.set_item_num(8, i, count_chars)
                table.set_item_num(9, i, count_chars, count_chars_total)
                # Type-Token Ratio
                table.set_item_num(10, i, ttr)
                # Type-Token Ratio (Standardized)
                table.set_item_num(11, i, sttr)

                # Paragraph Length
                if count_paras == 0:
                    table.set_item_num(12, i, 0)
                    table.set_item_num(13, i, 0)
                    table.set_item_num(14, i, 0)
                    table.set_item_num(15, i, 0)
                else:
                    table.set_item_num(12, i, numpy.mean(len_paras_in_sentence))
                    table.set_item_num(13, i, numpy.std(len_paras_in_sentence))
                    table.set_item_num(14, i, numpy.mean(len_paras_in_token))
                    table.set_item_num(15, i, numpy.std(len_paras_in_token))

                # Sentence Length
                if count_sentences == 0:
                    table.set_item_num(16, i, 0)
                    table.set_item_num(17, i, 0)
                else:
                    table.set_item_num(16, i, numpy.mean(len_sentences))
                    table.set_item_num(17, i, numpy.std(len_sentences))

                # Token Length
                if count_tokens == 0:
                    table.set_item_num(18, i, 0)
                    table.set_item_num(19, i, 0)
                else:
                    table.set_item_num(18, i, numpy.mean(len_tokens))
                    table.set_item_num(19, i, numpy.std(len_tokens))

                # Type Length
                if count_types == 0:
                    table.set_item_num(20, i, 0)
                    table.set_item_num(21, i, 0)
                else:
                    table.set_item_num(20, i, numpy.mean(len_types))
                    table.set_item_num(21, i, numpy.std(len_types))

                count_tokens_lens.append(collections.Counter(len_tokens))
                count_sentences_lens.append(collections.Counter(len_sentences))

            len_files = len(files)

            # Count of n-length Tokens
            if any(count_tokens_lens):
                count_tokens_lens_files = wl_misc.merge_dicts(count_tokens_lens)
                count_tokens_lens_total = {
                    len_token: count_tokens_files[-1]
                    for len_token, count_tokens_files in count_tokens_lens_files.items()
                }
                len_tokens_max = max(count_tokens_lens_files)
                
                for i in range(len_tokens_max):
                    table.insert_row(
                        table.rowCount(),
                        main.tr(f'Count of {i + 1}-Length Tokens'),
                        is_int = True, is_cumulative = True
                    )
                    table.insert_row(
                        table.rowCount(),
                        main.tr(f'Count of {i + 1}-Length Tokens %'),
                        is_pct = True, is_cumulative = True
                    )

                for i in range(len_tokens_max):
                    counts = count_tokens_lens_files.get(i + 1, [0] * (len_files + 1))

                    for j, count in enumerate(counts):
                        table.set_item_num(
                            row = table.rowCount() - (len_tokens_max - i) * 2,
                            col = j,
                            val = count
                        )
                        table.set_item_num(
                            row = table.rowCount() - (len_tokens_max - i) * 2 + 1,
                            col = j,
                            val = count,
                            total = count_tokens_lens_total.get(i + 1, 0)
                        )

            # Count of n-length Sentences
            if any(count_sentences_lens):
                count_sentences_lens_files = wl_misc.merge_dicts(count_sentences_lens)
                count_sentences_lens_total = {
                    len_sentence: count_sentences_files[-1]
                    for len_sentence, count_sentences_files in count_sentences_lens_files.items()
                }
                len_sentences_max = max(count_sentences_lens_files)
                
                for i in range(len_sentences_max):
                    table.insert_row(
                        table.rowCount(),
                        main.tr(f'Count of {i + 1}-Length Sentences'),
                        is_int = True, is_cumulative = True
                    )
                    table.insert_row(
                        table.rowCount(),
                        main.tr(f'Count of {i + 1}-Length Sentences %'),
                        is_pct = True, is_cumulative = True
                    )

                for i in range(len_sentences_max):
                    counts = count_sentences_lens_files.get(i + 1, [0] * (len_files + 1))

                    for j, count in enumerate(counts):
                        table.set_item_num(
                            row = table.rowCount() - (len_sentences_max - i) * 2,
                            col = j,
                            val = count
                        )
                        table.set_item_num(
                            row = table.rowCount() - (len_sentences_max - i) * 2 + 1,
                            col = j,
                            val = count,
                            total = count_sentences_lens_total.get(i + 1, 0)
                        )

            table.setUpdatesEnabled(True)
            table.blockSignals(False)

            table.toggle_pct()
            table.toggle_cumulative()
            table.toggle_breakdown()

            table.itemChanged.emit(table.item(0, 0))

            wl_msg.wl_msg_generate_table_success(main)
        else:
            wl_msg_box.wl_msg_box_no_results(main)

            wl_msg.wl_msg_generate_table_error(main)

    settings = main.settings_custom['overview']
    files = main.wl_files.get_selected_files()

    for file in files:
        if re.search(r'\.xml$', file['path'], flags = re.IGNORECASE):
            if file['tokenized'] == 'No' or file['tagged'] == 'No':
                wl_msg_box.wl_msg_box_invalid_xml_file(main)

                return

    dialog_progress = wl_dialog_misc.Wl_Dialog_Progress_Process_Data(main)

    worker_overview_table = Wl_Worker_Overview_Table(
        main,
        dialog_progress = dialog_progress,
        update_gui = update_gui
    )

    thread_overview_table = wl_threading.Wl_Thread(worker_overview_table)
    thread_overview_table.start_worker()
