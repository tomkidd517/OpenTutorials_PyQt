#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class MenuBarWidget(QMenuBar):
	def __init__(self):
		QMenuBar.__init__(self)
		self.init_menu_file()
		self.init_menu_edit()
		self.init_menu_format()
		self.init_menu_view()
		self.init_menu_help()

	def init_menu_file(self):
		# Action 설정
		# 새 파일
		self.act_new_file = QAction(self.tr('New') + "(&N)", self)
		self.act_new_file.setShortcut(QKeySequence('Ctrl+N'))
		self.act_new_file.triggered.connect(self.slot_new)
		# 열기
		self.act_open_file = QAction(self.tr('Open...')+ "(&O)", self)
		self.act_open_file.setShortcut(QKeySequence('Ctrl+O'))
		self.act_open_file.triggered.connect(self.slot_open)
		# 저장
		self.act_save_file = QAction(self.tr('Save')+ "(&S)", self)
		self.act_save_file.setShortcut(QKeySequence('Ctrl+S'))
		self.act_save_file.triggered.connect(self.slot_save)
		# 다른 이름으로 저장
		self.act_save_as_file = QAction(self.tr('Save as...') + "(&A)", self)
		self.act_save_as_file.triggered.connect(self.slot_save_as)
		# 페이지 설정
		self.act_page_setup = QAction(self.tr('Page Setup...') + "(&U)", self)
		self.act_page_setup.setShortcut(QKeySequence('Ctrl+S'))
		self.act_page_setup.triggered.connect(self.slot_page_setup)
		# 프린트
		self.act_print = QAction(self.tr('Print...') + "(&P)", self)
		self.act_print.setShortcut(QKeySequence('Ctrl+P'))
		self.act_print.triggered.connect(self.slot_print)
		# 끝내기
		self.act_quit = QAction(self.tr('Exit') + "(&X)", self)
		self.act_quit.triggered.connect(self.slot_quit)
		# 메뉴바 생성 및 액션 적용
		# addAction한 차례로 삽입

		menu_file = self.addMenu(self.tr("File") + "(&F)")
		menu_file.addAction(self.act_new_file)
		menu_file.addAction(self.act_open_file)
		menu_file.addAction(self.act_save_file)
		menu_file.addAction(self.act_save_as_file)
		menu_file.addSeparator()
		menu_file.addAction(self.act_page_setup)
		menu_file.addAction(self.act_print)
		menu_file.addSeparator()
		menu_file.addAction(self.act_quit)

	def init_menu_edit(self):
		# 실행취소
		self.act_undo = QAction(self.tr('Undo'), self)
		self.act_undo.setShortcut(QKeySequence('Ctrl+Z'))
		self.act_undo.triggered.connect(self.slot_undo)
		# 잘라내기
		self.act_cut = QAction(self.tr('Cut'), self)
		self.act_cut.setShortcut(QKeySequence('Ctrl+X'))
		self.act_cut.triggered.connect(self.slot_cut)
		# 복사
		self.act_copy = QAction(self.tr('Copy'), self)
		self.act_copy.setShortcut(QKeySequence('Ctrl+C'))
		self.act_copy.triggered.connect(self.slot_copy)
		# 붙여넣기
		self.act_paste = QAction(self.tr('Paste'), self)
		self.act_paste.setShortcut(QKeySequence('Ctrl+V'))
		self.act_paste.triggered.connect(self.slot_paste)
		# 삭제
		self.act_del = QAction(self.tr('Del'), self)
		self.act_del.setShortcut(QKeySequence('Del'))
		self.act_del.triggered.connect(self.slot_del)
		# 찾기
		self.act_find = QAction(self.tr('Find...'), self)
		self.act_find.setShortcut(QKeySequence('Ctrl+F'))
		self.act_find.triggered.connect(self.slot_find)
		# 다음찾기
		self.act_find_next = QAction(self.tr('Find Next'), self)
		self.act_find_next.setShortcut(QKeySequence('F3'))
		self.act_find_next.triggered.connect(self.slot_find_next)
		# 바꾸기
		self.act_replace = QAction(self.tr('Replace...'), self)
		self.act_replace.setShortcut(QKeySequence('Ctrl+H'))
		self.act_replace.triggered.connect(self.slot_replace)
		# 이동
		self.act_go_to = QAction(self.tr('Go To...'), self)
		self.act_go_to.setShortcut(QKeySequence('Ctrl+G'))
		self.act_go_to.triggered.connect(self.slot_go_to)
		# 모두선택
		self.act_select_all = QAction(self.tr('Select All'), self)
		self.act_select_all.setShortcut(QKeySequence('Ctrl+A'))
		self.act_select_all.triggered.connect(self.slot_select_all)
		# 시간날짜
		self.act_time_date = QAction(self.tr('Time/Date'), self)
		self.act_time_date.setShortcut(QKeySequence('F5'))
		self.act_time_date.triggered.connect(self.slot_time_date)

		menu_file = self.addMenu(self.tr('Edit') + "(&E)")
		menu_file.addAction(self.act_undo)
		menu_file.addSeparator()
		menu_file.addAction(self.act_cut)
		menu_file.addAction(self.act_copy)
		menu_file.addAction(self.act_paste)
		menu_file.addAction(self.act_del)
		menu_file.addSeparator()
		menu_file.addAction(self.act_find)
		menu_file.addAction(self.act_find_next)
		menu_file.addAction(self.act_replace)
		menu_file.addAction(self.act_go_to)
		menu_file.addSeparator()
		menu_file.addAction(self.act_select_all)
		menu_file.addAction(self.act_time_date)

	def init_menu_format(self):
		# 자동 줄 바꾹
		self.act_word_wrap = QAction(self.tr('Word Wrap'), self)
		self.act_word_wrap.triggered.connect(self.slot_word_wrap)
		# 글꼴
		self.act_font = QAction(self.tr('Font...'), self)
		self.act_font.triggered.connect(self.slot_font)

		menu_file = self.addMenu(self.tr('Format') + "(&O)")
		menu_file.addAction(self.act_word_wrap)
		menu_file.addAction(self.act_font)

	def init_menu_view(self):
		self.act_status_bar = QAction(self.tr('Status Bar'), self)
		self.act_status_bar.triggered.connect(self.slot_status_bar)

		menu_file = self.addMenu(self.tr('View') + "(&V)")
		menu_file.addAction(self.act_status_bar)

	def init_menu_help(self):
		self.act_help = QAction(self.tr('Help'), self)
		self.act_help.triggered.connect(self.slot_help)
		# 메모장 정보
		self.act_about = QAction(self.tr('About'), self)
		self.act_about.triggered.connect(self.slot_about)

		menu_file = self.addMenu(self.tr('Help') + "(&H)")
		menu_file.addAction(self.act_help)
		menu_file.addSeparator()
		menu_file.addAction(self.act_about)

	@pyqtSlot()
	def slot_new(self):
		pass

	@pyqtSlot()
	def slot_open(self):
		pass

	@pyqtSlot()
	def slot_save(self):
		pass

	@pyqtSlot()
	def slot_save_as(self):
		pass

	@pyqtSlot()
	def slot_page_setup(self):
		pass

	@pyqtSlot()
	def slot_print(self):
		pass

	@pyqtSlot()
	def slot_quit(self):
		pass

	@pyqtSlot()
	def slot_undo(self):
		pass

	@pyqtSlot()
	def slot_cut(self):
		pass

	@pyqtSlot()
	def slot_copy(self):
		pass

	@pyqtSlot()
	def slot_paste(self):
		pass

	@pyqtSlot()
	def slot_del(self):
		pass

	@pyqtSlot()
	def slot_find(self):
		pass

	@pyqtSlot()
	def slot_find_next(self):
		pass

	@pyqtSlot()
	def slot_replace(self):
		pass

	@pyqtSlot()
	def slot_go_to(self):
		pass

	@pyqtSlot()
	def slot_select_all(self):
		pass

	@pyqtSlot()
	def slot_time_date(self):
		pass

	@pyqtSlot()
	def slot_word_wrap(self):
		pass

	@pyqtSlot()
	def slot_font(self):
		pass

	@pyqtSlot()
	def slot_status_bar(self):
		pass

	@pyqtSlot()
	def slot_help(self):
		pass

	@pyqtSlot()
	def slot_about(self):
		pass

	def retranslate_ui(self):
		self.clear()
		self.init_menu_file()
		self.init_menu_edit()
		self.init_menu_format()
		self.init_menu_view()
		self.init_menu_help()

if __name__ == "__main__":
	from PyQt5.QtWidgets import QMainWindow
	from PyQt5.QtCore import Qt


	class Form(QMainWindow):
		def __init__(self):
			QMainWindow.__init__(self, flags=Qt.Window)
			self.filename = "제목없음"
			self.init_window()

		def init_window(self):
			"""
			현재 위젯의 모양등을 초기화
			"""
			self.setWindowTitle("제목 없음 - 메모장")
			self.resize(640, 480)

			self.menu = MenuBarWidget()
			self.setMenuBar(self.menu)

	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())