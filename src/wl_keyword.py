#
# Wordless: Keyword
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
import re
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy

from wl_checking import wl_checking_file
from wl_dialogs import wl_dialog_misc, wl_msg_box
from wl_figs import wl_fig, wl_fig_freq, wl_fig_stat
from wl_text import wl_text, wl_text_utils, wl_token_processing
from wl_utils import wl_misc, wl_sorting, wl_threading
from wl_widgets import wl_box, wl_layout, wl_msg, wl_table, wl_widgets

class Wl_Table_Keyword(wl_table.Wl_Table_Data_Filter_Search):
    def __init__(self, parent):
        super().__init__(
            parent,
            tab = 'keyword',
            headers = [
                parent.tr('Rank'),
                parent.tr('Keyword'),
                parent.tr('Number of\nFiles Found'),
                parent.tr('Number of\nFiles Found %')
            ],
            headers_int = [
                parent.tr('Rank'),
                parent.tr('Number of\nFiles Found')
            ],
            headers_pct = [
                parent.tr('Number of\nFiles Found %')
            ],
            sorting_enabled = True
        )

        self.name = 'keyword'

        self.button_generate_table = QPushButton(self.tr('Generate Table'), self)
        self.button_generate_fig = QPushButton(self.tr('Generate Figure'), self)

        self.button_generate_table.clicked.connect(lambda: generate_table(self.main, self))
        self.button_generate_fig.clicked.connect(lambda: generate_fig(self.main))

class Wrapper_Keyword(wl_layout.Wl_Wrapper):
    def __init__(self, main):
        super().__init__(main)

        # Table
        self.table_keyword = Wl_Table_Keyword(self)

        layout_results = wl_layout.Wl_Layout()
        layout_results.addWidget(self.table_keyword.label_number_results, 0, 0)
        layout_results.addWidget(self.table_keyword.button_results_filter, 0, 2)
        layout_results.addWidget(self.table_keyword.button_results_search, 0, 3)

        layout_results.setColumnStretch(1, 1)

        self.wrapper_table.layout().addLayout(layout_results, 0, 0, 1, 5)
        self.wrapper_table.layout().addWidget(self.table_keyword, 1, 0, 1, 5)
        self.wrapper_table.layout().addWidget(self.table_keyword.button_generate_table, 2, 0)
        self.wrapper_table.layout().addWidget(self.table_keyword.button_generate_fig, 2, 1)
        self.wrapper_table.layout().addWidget(self.table_keyword.button_export_selected, 2, 2)
        self.wrapper_table.layout().addWidget(self.table_keyword.button_export_all, 2, 3)
        self.wrapper_table.layout().addWidget(self.table_keyword.button_clear, 2, 4)

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
        self.group_box_generation_settings = QGroupBox(self.tr('Generation Settings'))

        self.label_ref_file = QLabel(self.tr('Reference File:'), self)
        self.combo_box_ref_file = wl_box.Wl_Combo_Box_Ref_File(self)
        (self.label_test_significance,
         self.combo_box_test_significance) = wl_widgets.wl_widgets_test_significance(self)
        (self.label_measure_effect_size,
         self.combo_box_measure_effect_size) = wl_widgets.wl_widgets_measure_effect_size(self)

        (self.label_settings_measures,
         self.button_settings_measures) = wl_widgets.wl_widgets_settings_measures(
            self,
            tab = self.tr('Statistical Significance')
        )

        self.combo_box_test_significance.addItems(list(self.main.settings_global['tests_significance']['keyword'].keys()))
        self.combo_box_measure_effect_size.addItems(list(self.main.settings_global['measures_effect_size']['keyword'].keys()))

        self.combo_box_ref_file.currentTextChanged.connect(self.generation_settings_changed)
        self.combo_box_test_significance.currentTextChanged.connect(self.generation_settings_changed)
        self.combo_box_measure_effect_size.currentTextChanged.connect(self.generation_settings_changed)

        layout_settings_measures = wl_layout.Wl_Layout()
        layout_settings_measures.addWidget(self.label_settings_measures, 0, 0)
        layout_settings_measures.addWidget(self.button_settings_measures, 0, 1)

        layout_settings_measures.setColumnStretch(1, 1)

        self.group_box_generation_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_generation_settings.layout().addWidget(self.label_ref_file, 0, 0)
        self.group_box_generation_settings.layout().addWidget(self.combo_box_ref_file, 1, 0)
        self.group_box_generation_settings.layout().addWidget(self.label_test_significance, 3, 0)
        self.group_box_generation_settings.layout().addWidget(self.combo_box_test_significance, 4, 0)
        self.group_box_generation_settings.layout().addWidget(self.label_measure_effect_size, 5, 0)
        self.group_box_generation_settings.layout().addWidget(self.combo_box_measure_effect_size, 6, 0)

        self.group_box_generation_settings.layout().addWidget(wl_layout.Wl_Separator(self), 7, 0)

        self.group_box_generation_settings.layout().addLayout(layout_settings_measures, 8, 0)

        # Table Settings
        self.group_box_table_settings = QGroupBox(self.tr('Table Settings'))

        (self.checkbox_show_pct,
         self.checkbox_show_cumulative,
         self.checkbox_show_breakdown) = wl_widgets.wl_widgets_table_settings(
            self,
            table = self.table_keyword
        )

        self.checkbox_show_pct.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_cumulative.stateChanged.connect(self.table_settings_changed)
        self.checkbox_show_breakdown.stateChanged.connect(self.table_settings_changed)

        self.group_box_table_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_pct, 0, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_cumulative, 1, 0)
        self.group_box_table_settings.layout().addWidget(self.checkbox_show_breakdown, 2, 0)

        # Figure Settings
        self.group_box_fig_settings = QGroupBox(self.tr('Figure Settings'), self)

        (self.label_graph_type,
         self.combo_box_graph_type,
         self.label_use_file,
         self.combo_box_use_file,
         self.label_use_data,
         self.combo_box_use_data,

         self.checkbox_use_pct,
         self.checkbox_use_cumulative) = wl_widgets.wl_widgets_fig_settings(self)

        self.label_rank = QLabel(self.tr('Rank:'), self)
        (self.label_rank_min,
         self.spin_box_rank_min,
         self.checkbox_rank_min_no_limit,
         self.label_rank_max,
         self.spin_box_rank_max,
         self.checkbox_rank_max_no_limit) = wl_widgets.wl_widgets_filter(
            self,
            filter_min = 1,
            filter_max = 100000
        )

        self.combo_box_graph_type.currentTextChanged.connect(self.fig_settings_changed)
        self.combo_box_use_file.currentTextChanged.connect(self.fig_settings_changed)
        self.combo_box_use_data.currentTextChanged.connect(self.fig_settings_changed)
        self.checkbox_use_pct.stateChanged.connect(self.fig_settings_changed)
        self.checkbox_use_cumulative.stateChanged.connect(self.fig_settings_changed)

        self.spin_box_rank_min.valueChanged.connect(self.fig_settings_changed)
        self.checkbox_rank_min_no_limit.stateChanged.connect(self.fig_settings_changed)
        self.spin_box_rank_max.valueChanged.connect(self.fig_settings_changed)
        self.checkbox_rank_max_no_limit.stateChanged.connect(self.fig_settings_changed)

        layout_fig_settings_combo_boxes = wl_layout.Wl_Layout()
        layout_fig_settings_combo_boxes.addWidget(self.label_graph_type, 0, 0)
        layout_fig_settings_combo_boxes.addWidget(self.combo_box_graph_type, 0, 1)
        layout_fig_settings_combo_boxes.addWidget(self.label_use_file, 1, 0)
        layout_fig_settings_combo_boxes.addWidget(self.combo_box_use_file, 1, 1)
        layout_fig_settings_combo_boxes.addWidget(self.label_use_data, 2, 0)
        layout_fig_settings_combo_boxes.addWidget(self.combo_box_use_data, 2, 1)

        layout_fig_settings_combo_boxes.setColumnStretch(1, 1)

        self.group_box_fig_settings.setLayout(wl_layout.Wl_Layout())
        self.group_box_fig_settings.layout().addLayout(layout_fig_settings_combo_boxes, 0, 0, 1, 3)
        self.group_box_fig_settings.layout().addWidget(self.checkbox_use_pct, 1, 0, 1, 3)
        self.group_box_fig_settings.layout().addWidget(self.checkbox_use_cumulative, 2, 0, 1, 3)
        
        self.group_box_fig_settings.layout().addWidget(wl_layout.Wl_Separator(self), 3, 0, 1, 3)

        self.group_box_fig_settings.layout().addWidget(self.label_rank, 4, 0, 1, 3)
        self.group_box_fig_settings.layout().addWidget(self.label_rank_min, 5, 0)
        self.group_box_fig_settings.layout().addWidget(self.spin_box_rank_min, 5, 1)
        self.group_box_fig_settings.layout().addWidget(self.checkbox_rank_min_no_limit, 5, 2)
        self.group_box_fig_settings.layout().addWidget(self.label_rank_max, 6, 0)
        self.group_box_fig_settings.layout().addWidget(self.spin_box_rank_max, 6, 1)
        self.group_box_fig_settings.layout().addWidget(self.checkbox_rank_max_no_limit, 6, 2)

        self.group_box_fig_settings.layout().setColumnStretch(1, 1)

        self.wrapper_settings.layout().addWidget(self.group_box_token_settings, 0, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_generation_settings, 1, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_table_settings, 2, 0)
        self.wrapper_settings.layout().addWidget(self.group_box_fig_settings, 3, 0)

        self.wrapper_settings.layout().setRowStretch(4, 1)

        self.load_settings()

    def load_settings(self, defaults = False):
        if defaults:
            settings = copy.deepcopy(self.main.settings_default['keyword'])
        else:
            settings = copy.deepcopy(self.main.settings_custom['keyword'])

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
        self.combo_box_ref_file.setCurrentText(settings['generation_settings']['ref_file'])
        self.combo_box_test_significance.setCurrentText(settings['generation_settings']['test_significance'])
        self.combo_box_measure_effect_size.setCurrentText(settings['generation_settings']['measure_effect_size'])

        # Table Settings
        self.checkbox_show_pct.setChecked(settings['table_settings']['show_pct'])
        self.checkbox_show_cumulative.setChecked(settings['table_settings']['show_cumulative'])
        self.checkbox_show_breakdown.setChecked(settings['table_settings']['show_breakdown'])

        # Figure Settings
        self.combo_box_graph_type.setCurrentText(settings['fig_settings']['graph_type'])
        self.combo_box_use_file.setCurrentText(settings['fig_settings']['use_file'])
        self.combo_box_use_data.setCurrentText(settings['fig_settings']['use_data'])
        self.checkbox_use_pct.setChecked(settings['fig_settings']['use_pct'])
        self.checkbox_use_cumulative.setChecked(settings['fig_settings']['use_cumulative'])

        self.spin_box_rank_min.setValue(settings['fig_settings']['rank_min'])
        self.checkbox_rank_min_no_limit.setChecked(settings['fig_settings']['rank_min_no_limit'])
        self.spin_box_rank_max.setValue(settings['fig_settings']['rank_max'])
        self.checkbox_rank_max_no_limit.setChecked(settings['fig_settings']['rank_max_no_limit'])

        self.token_settings_changed()
        self.generation_settings_changed()
        self.table_settings_changed()
        self.fig_settings_changed()

    def token_settings_changed(self):
        settings = self.main.settings_custom['keyword']['token_settings']

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

    def generation_settings_changed(self):
        settings = self.main.settings_custom['keyword']['generation_settings']

        if self.combo_box_ref_file.currentText() == self.tr('*** None ***'):
            settings['ref_file'] = ''
        else:
            settings['ref_file'] = self.combo_box_ref_file.currentText()

        settings['test_significance'] = self.combo_box_test_significance.currentText()
        settings['measure_effect_size'] = self.combo_box_measure_effect_size.currentText()

        # Use File
        use_file_old = self.combo_box_use_file.currentText()

        self.combo_box_use_file.wl_files_changed()

        self.combo_box_use_file.removeItem(self.combo_box_use_file.findText(settings['ref_file']))

        if self.combo_box_use_file.findText(use_file_old) > -1:
            self.combo_box_use_file.setCurrentText(use_file_old)
        else:
            self.combo_box_use_file.setCurrentIndex(0)

        # Use Data
        use_data_old = self.combo_box_use_data.currentText()

        text_test_significance = settings['test_significance']
        text_measure_effect_size = settings['measure_effect_size']

        self.combo_box_use_data.clear()

        self.combo_box_use_data.addItem(self.tr('Frequency'))
        self.combo_box_use_data.addItems(
            [col
             for col in self.main.settings_global['tests_significance']['keyword'][text_test_significance]['cols']
             if col]
        )
        self.combo_box_use_data.addItem(self.main.settings_global['measures_effect_size']['keyword'][text_measure_effect_size]['col'])

        if self.combo_box_use_data.findText(use_data_old) > -1:
            self.combo_box_use_data.setCurrentText(use_data_old)
        else:
            self.combo_box_use_data.setCurrentText(self.main.settings_default['keyword']['fig_settings']['use_data'])

    def table_settings_changed(self):
        settings = self.main.settings_custom['keyword']['table_settings']

        settings['show_pct'] = self.checkbox_show_pct.isChecked()
        settings['show_cumulative'] = self.checkbox_show_cumulative.isChecked()
        settings['show_breakdown'] = self.checkbox_show_breakdown.isChecked()

    def fig_settings_changed(self):
        settings = self.main.settings_custom['keyword']['fig_settings']

        settings['graph_type'] = self.combo_box_graph_type.currentText()
        settings['use_file'] = self.combo_box_use_file.currentText()
        settings['use_data'] = self.combo_box_use_data.currentText()
        settings['use_pct'] = self.checkbox_use_pct.isChecked()
        settings['use_cumulative'] = self.checkbox_use_cumulative.isChecked()

        settings['rank_min'] = self.spin_box_rank_min.value()
        settings['rank_min_no_limit'] = self.checkbox_rank_min_no_limit.isChecked()
        settings['rank_max'] = self.spin_box_rank_max.value()
        settings['rank_max_no_limit'] = self.checkbox_rank_max_no_limit.isChecked()

class Wl_Worker_Keyword(wl_threading.Wl_Worker):
    worker_done = pyqtSignal(dict, dict)

    def __init__(self, main, dialog_progress, update_gui):
        super().__init__(main, dialog_progress, update_gui)

        self.keywords_freq_files = []
        self.keywords_stats_files = []

    def run(self):
        texts = []

        settings = self.main.settings_custom['keyword']
        ref_file = self.main.wl_files.find_file_by_name(
            settings['generation_settings']['ref_file'],
            selected_only = True
        )

        files = [file
                 for file in self.main.wl_files.get_selected_files()
                 if file != ref_file]

        # Frequency
        for i, file in enumerate([ref_file] + files):
            text = wl_text.Wl_Text(self.main, file)
            text = wl_token_processing.wl_process_tokens_keyword(
                text,
                token_settings = settings['token_settings']
            )

            # Remove empty tokens
            tokens = [token for token in text.tokens_flat if token]

            self.keywords_freq_files.append(collections.Counter(tokens))

            if i > 0:
                texts.append(text)
            else:
                tokens_ref = text.tokens_flat.copy()
                len_tokens_ref = len(tokens_ref)

        # Total
        if len(files) > 1:
            text_total = wl_text.Wl_Text_Blank()
            text_total.tokens_flat = [token for text in texts for token in text.tokens_flat]

            self.keywords_freq_files.append(sum(self.keywords_freq_files, collections.Counter()))

            self.keywords_freq_files[0] = {token: freq
                                           for token, freq in self.keywords_freq_files[0].items()
                                           if token in text_total.tokens_flat}

            texts.append(text_total)
        else:
            self.keywords_freq_files[0] = {token: freq
                                           for token, freq in self.keywords_freq_files[0].items()
                                           if token in self.keywords_freq_files[1]}

        self.progress_updated.emit(self.tr('Processing data ...'))

        # Keyness
        text_test_significance = settings['generation_settings']['test_significance']
        text_measure_effect_size = settings['generation_settings']['measure_effect_size']

        test_significance = self.main.settings_global['tests_significance']['keyword'][text_test_significance]['func']
        measure_effect_size = self.main.settings_global['measures_effect_size']['keyword'][text_measure_effect_size]['func']

        keywords_freq_file_observed = self.keywords_freq_files[-1]
        keywords_freq_file_ref = self.keywords_freq_files[0]

        for text in texts:
            keywords_stats_file = {}

            tokens_observed = text.tokens_flat
            len_tokens_observed = len(tokens_observed)

            if text_test_significance in [self.tr('Student\'s t-test (Two-sample)'),
                                          self.tr('Mann-Whitney U Test')]:
                # Test Statistic, p-value & Bayes Factor
                if text_test_significance == self.tr('Student\'s t-test (Two-sample)'):
                    number_sections = self.main.settings_custom['measures']['statistical_significance']['students_t_test_2_sample']['number_sections']
                    use_data = self.main.settings_custom['measures']['statistical_significance']['students_t_test_2_sample']['use_data']
                elif text_test_significance == self.tr('Mann-Whitney U Test'):
                    number_sections = self.main.settings_custom['measures']['statistical_significance']['mann_whitney_u_test']['number_sections']
                    use_data = self.main.settings_custom['measures']['statistical_significance']['mann_whitney_u_test']['use_data']

                sections_observed = wl_text_utils.to_sections(tokens_observed, number_sections)
                sections_ref = wl_text_utils.to_sections(tokens_ref, number_sections)

                sections_freq_observed = [collections.Counter(section) for section in sections_observed]
                sections_freq_ref = [collections.Counter(section) for section in sections_observed]

                len_sections_observed = [len(section) for section in sections_observed]
                len_sections_ref = [len(section) for section in sections_ref]

                if use_data == self.tr('Absolute Frequency'):
                    for token in keywords_freq_file_observed:
                        counts_observed = [section_freq.get(token, 0) for section_freq in sections_freq_observed]
                        counts_ref = [section_freq.get(token, 0) for section_freq in sections_freq_ref]

                        keywords_stats_file[token] = test_significance(self.main, counts_observed, counts_ref)
                elif use_data == self.tr('Relative Frequency'):
                    for token in keywords_freq_file_observed:
                        counts_observed = [section_freq.get(token, 0) / len_sections_observed[i]
                                           for i, section_freq in enumerate(sections_freq_observed)]
                        counts_ref = [section_freq.get(token, 0) / len_sections_ref[i]
                                      for i, section_freq in enumerate(sections_freq_ref)]

                        keywords_stats_file[token] = test_significance(self.main, counts_observed, counts_ref)

                # Effect Size
                for token in keywords_freq_file_observed:
                    c11 = keywords_freq_file_observed.get(token, 0)
                    c12 = keywords_freq_file_ref.get(token, 0)
                    c21 = len_tokens_observed - c11
                    c22 = len_tokens_ref - c12

                    keywords_stats_file[token].append(measure_effect_size(self.main, c11, c12, c21, c22))
            else:
                for token in keywords_freq_file_observed:
                    c11 = keywords_freq_file_observed.get(token, 0)
                    c12 = keywords_freq_file_ref.get(token, 0)
                    c21 = len_tokens_observed - c11
                    c22 = len_tokens_ref - c12

                    # Test Statistic, p-value & Bayes Factor
                    keywords_stats_file[token] = test_significance(self.main, c11, c12, c21, c22)

                    # Effect Size
                    keywords_stats_file[token].append(measure_effect_size(self.main, c11, c12, c21, c22))

            self.keywords_stats_files.append(keywords_stats_file)

        if len(files) == 1:
            self.keywords_freq_files.append(self.keywords_freq_files[1])
            self.keywords_stats_files *= 2

class Wl_Worker_Keyword_Table(Wl_Worker_Keyword):
    def run(self):
        super().run()

        self.progress_updated.emit(self.tr('Rendering table ...'))

        time.sleep(0.1)

        self.worker_done.emit(wl_misc.merge_dicts(self.keywords_freq_files),
                              wl_misc.merge_dicts(self.keywords_stats_files))

class Wl_Worker_Keyword_Fig(Wl_Worker_Keyword):
    def run(self):
        super().run()

        self.progress_updated.emit(self.tr('Rendering figure ...'))

        time.sleep(0.1)

        self.worker_done.emit(wl_misc.merge_dicts(self.keywords_freq_files),
                              wl_misc.merge_dicts(self.keywords_stats_files))

@wl_misc.log_timing
def generate_table(main, table):
    def update_gui(keywords_freq_files, keywords_stats_files):
        if keywords_freq_files:
            table.clear_table()

            table.settings = copy.deepcopy(main.settings_custom)

            text_test_significance = settings['generation_settings']['test_significance']
            text_measure_effect_size = settings['generation_settings']['measure_effect_size']

            (text_test_stat,
             text_p_value,
             text_bayes_factor) = main.settings_global['tests_significance']['keyword'][text_test_significance]['cols']
            text_effect_size =  main.settings_global['measures_effect_size']['keyword'][text_measure_effect_size]['col']

            # Insert columns (files)
            table.insert_col(table.columnCount() - 2,
                             main.tr(f'[{ref_file["name"]}]\nFrequency'),
                             is_int = True, is_cumulative = True)
            table.insert_col(table.columnCount() - 2,
                             main.tr(f'[{ref_file["name"]}]\nFrequency %'),
                             is_pct = True, is_cumulative = True)

            for file in files:
                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'[{file["name"]}]\nFrequency'),
                                 is_int = True, is_cumulative = True, is_breakdown = True)
                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'[{file["name"]}]\nFrequency %'),
                                 is_pct = True, is_cumulative = True, is_breakdown = True)

                if text_test_stat:
                    table.insert_col(table.columnCount() - 2,
                                     main.tr(f'[{file["name"]}]\n{text_test_stat}'),
                                     is_float = True, is_breakdown = True)

                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'[{file["name"]}]\n{text_p_value}'),
                                 is_float = True, is_breakdown = True)

                if text_bayes_factor:
                    table.insert_col(table.columnCount() - 2,
                                     main.tr(f'[{file["name"]}]\n{text_bayes_factor}'),
                                     is_float = True, is_breakdown = True)

                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'[{file["name"]}]\n{text_effect_size}'),
                                 is_float = True, is_breakdown = True)

            # Insert columns (total)
            table.insert_col(table.columnCount() - 2,
                             main.tr('Total\nFrequency'),
                             is_int = True, is_cumulative = True)
            table.insert_col(table.columnCount() - 2,
                             main.tr('Total\nFrequency %'),
                             is_pct = True, is_cumulative = True)

            if text_test_stat:
                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'Total\n{text_test_stat}'),
                                 is_float = True)

            table.insert_col(table.columnCount() - 2,
                             main.tr(f'Total\n{text_p_value}'),
                             is_float = True)

            if text_bayes_factor:
                table.insert_col(table.columnCount() - 2,
                                 main.tr(f'Total\n{text_bayes_factor}'),
                                 is_float = True)

            table.insert_col(table.columnCount() - 2,
                             main.tr(f'Total\n{text_effect_size}'),
                             is_float = True)

            # Sort by p-value of the first file
            table.horizontalHeader().setSortIndicator(
                table.find_col(main.tr(f'[{files[0]["name"]}]\n{text_p_value}')),
                Qt.AscendingOrder
            )

            table.blockSignals(True)
            table.setSortingEnabled(False)
            table.setUpdatesEnabled(False)

            cols_freq = table.find_cols(main.tr('\nFrequency'))
            cols_freq_pct = table.find_cols(main.tr('\nFrequency %'))

            for col in cols_freq_pct:
                cols_freq.remove(col)

            if text_test_stat:
                cols_test_stat = table.find_cols(main.tr(f'\n{text_test_stat}'))

            cols_p_value = table.find_cols(main.tr('\np-value'))

            if text_bayes_factor:
                cols_bayes_factor = table.find_cols(main.tr('\nBayes Factor'))

            cols_effect_size = table.find_cols(f'\n{text_effect_size}')
            col_files_found = table.find_col(main.tr('Number of\nFiles Found'))
            col_files_found_pct = table.find_col(main.tr('Number of\nFiles Found %'))

            freq_totals = numpy.array(list(keywords_freq_files.values())).sum(axis = 0)
            len_files = len(files)

            table.setRowCount(len(keywords_freq_files))

            for i, (keyword, stats_files) in enumerate(wl_sorting.sorted_keywords_stats_files(keywords_stats_files)):
                freq_files = keywords_freq_files[keyword]

                # Rank
                table.set_item_num(i, 0, -1)

                # Keyword
                table.setItem(i, 1, wl_table.Wl_Table_Item(keyword))

                # Frequency
                for j, freq in enumerate(freq_files):
                    table.set_item_num(i, cols_freq[j], freq)
                    table.set_item_num(i, cols_freq_pct[j], freq, freq_totals[j])

                for j, (test_stat, p_value, bayes_factor, effect_size) in enumerate(stats_files):
                    # Test Statistic
                    if text_test_stat:
                        table.set_item_num(i, cols_test_stat[j], test_stat)

                    # p-value
                    table.set_item_num(i, cols_p_value[j], p_value)

                    # Bayes Factor
                    if text_bayes_factor:
                        table.set_item_num(i, cols_bayes_factor[j], bayes_factor)

                    # Effect Size
                    table.set_item_num(i, cols_effect_size[j], effect_size)

                # Number of Files Found
                num_files_found = len([freq for freq in freq_files[1:-1] if freq])

                table.set_item_num(i, col_files_found, num_files_found)
                table.set_item_num(i, col_files_found_pct, num_files_found, len_files)

            table.setSortingEnabled(True)
            table.setUpdatesEnabled(True)
            table.blockSignals(False)

            table.toggle_pct()
            table.toggle_cumulative()
            table.toggle_breakdown()
            table.update_ranks()

            table.itemChanged.emit(table.item(0, 0))

            wl_msg.wl_msg_generate_table_success(main)
        else:
            wl_msg_box.wl_msg_box_no_results(main)

            wl_msg.wl_msg_generate_table_error(main)

    settings = main.settings_custom['keyword']
    files = main.wl_files.get_selected_files()

    for file in files:
        if re.search(r'\.xml$', file['path'], flags = re.IGNORECASE):
            if file['tokenized'] == 'No' or file['tagged'] == 'No':
                wl_msg_box.wl_msg_box_invalid_xml_file(main)

                return

    ref_file = main.wl_files.find_file_by_name(
        settings['generation_settings']['ref_file'],
        selected_only = True
    )

    files = [file
             for file in main.wl_files.get_selected_files()
             if file != ref_file]

    if files:
        dialog_progress = wl_dialog_misc.Wl_Dialog_Progress_Process_Data(main)

        worker_keyword_table = Wl_Worker_Keyword_Table(
            main,
            dialog_progress = dialog_progress,
            update_gui = update_gui
        )

        thread_keyword_table = wl_threading.Wl_Thread(worker_keyword_table)
        thread_keyword_table.start_worker()
    else:
        wl_msg_box.wl_msg_box_missing_observed_file(main)

        wl_msg.wl_msg_generate_table_error(main)

@wl_misc.log_timing
def generate_fig(main):
    def update_gui(keywords_freq_files, keywords_stats_files):
        if keywords_freq_files:
            text_test_significance = settings['generation_settings']['test_significance']
            text_measure_effect_size = settings['generation_settings']['measure_effect_size']

            (text_test_stat,
             text_p_value,
             text_bayes_factor) = main.settings_global['tests_significance']['keyword'][text_test_significance]['cols']
            text_effect_size =  main.settings_global['measures_effect_size']['keyword'][text_measure_effect_size]['col']

            if settings['fig_settings']['use_data'] == main.tr('Frequency'):
                wl_fig_freq.wl_fig_freq_ref(
                    main, keywords_freq_files,
                    ref_file = ref_file,
                    settings = settings['fig_settings'],
                    label_x = main.tr('Keyword')
                )
            else:
                if settings['fig_settings']['use_data'] == text_test_stat:
                    keywords_stat_files = {
                        keyword: numpy.array(stats_files)[:, 0]
                        for keyword, stats_files in keywords_stats_files.items()
                    }

                    label_y = text_test_stat
                elif settings['fig_settings']['use_data'] == text_p_value:
                    keywords_stat_files = {
                        keyword: numpy.array(stats_files)[:, 1]
                        for keyword, stats_files in keywords_stats_files.items()
                    }

                    label_y = text_p_value
                elif settings['fig_settings']['use_data'] == text_bayes_factor:
                    keywords_stat_files = {
                        keyword: numpy.array(stats_files)[:, 2]
                        for keyword, stats_files in keywords_stats_files.items()
                    }

                    label_y = text_bayes_factor
                elif settings['fig_settings']['use_data'] == text_effect_size:
                    keywords_stat_files = {
                        keyword: numpy.array(stats_files)[:, 3]
                        for keyword, stats_files in keywords_stats_files.items()
                    }

                    label_y = text_effect_size

                wl_fig_stat.wl_fig_stat_ref(
                    main, keywords_stat_files,
                    ref_file = ref_file,
                    settings = settings['fig_settings'],
                    label_y = label_y
                )

            wl_msg.wl_msg_generate_fig_success(main)
        else:
            wl_msg_box.wl_msg_box_no_results(main)

            wl_msg.wl_msg_generate_fig_error(main)

        dialog_progress.accept()

        if keywords_freq_files:
            wl_fig.show_fig()

    settings = main.settings_custom['keyword']
    files = main.wl_files.get_selected_files()

    for file in files:
        if re.search(r'\.xml$', file['path'], flags = re.IGNORECASE):
            if file['tokenized'] == 'No' or file['tagged'] == 'No':
                wl_msg_box.wl_msg_box_invalid_xml_file(main)

                return
    
    ref_file = main.wl_files.find_file_by_name(
        settings['generation_settings']['ref_file'],
        selected_only = True
    )

    files = [file
             for file in main.wl_files.get_selected_files()
             if file != ref_file]

    if files:
        dialog_progress = wl_dialog_misc.Wl_Dialog_Progress_Process_Data(main)

        worker_keyword_fig = Wl_Worker_Keyword_Fig(
            main,
            dialog_progress = dialog_progress,
            update_gui = update_gui
        )

        thread_keyword_fig = wl_threading.Wl_Thread(worker_keyword_fig)
        thread_keyword_fig.start_worker()
    else:
        wl_msg_box.wl_msg_box_missing_observed_file(main)

        wl_msg.wl_msg_generate_fig_error(main)
