#!/usr/bin/env python3

import calendar
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from fpdf import FPDF

black = 0
white = 255
gray1 = 240
gray2 = 220
gray_break = 200
holiday_gray = 200

normal_line_width = 0.1
heavy_line_width = 0.4  # non-teaching days
week_col_width = 5
header_height = 6


def check_date_valid(year: int, month: int, day: int):
    date(year, month, day)  # will raise ValueError if out of range


class Semester:
    year: int = None
    start_month: int = None
    start_day: int = None
    weeks_long: int = None
    break_at_end_of_week: int = None
    assign_week_start: int = None
    semester_name: str = None

    due_dates = defaultdict(list)
    holidays = defaultdict(str)

    def __init__(self, year: int, month: int, day: int, semester_name: str = None):
        check_date_valid(year, month, day)
        self.year = year
        self.start_month = month
        self.start_day = day
        self.semester_name = semester_name
        if self.semester_name:
            self.due(month, day, f'{year} {semester_name}')

    def due(self, month: int, day: int, piece: str):
        check_date_valid(self.year, month, day)
        self.due_dates[(month, day)].append(piece)

    def holiday(self, month: int, day: int, name: str):
        check_date_valid(self.year, month, day)
        self.holidays[(month, day)] = name


class PDF(FPDF):

    def table(self, headings, rows):
        # Colors, line width and bold font:
        self.set_fill_color(gray2)
        self.set_text_color(black)
        self.set_draw_color(black)
        self.set_line_width(normal_line_width)
        self.set_font(style="B")
        col_width = (self.epw - week_col_width) / 7
        col_height = (self.eph - header_height - 2) / len(rows)
        self.cell(week_col_width, header_height, '', border=1, align="C", fill=True)
        for heading in headings:
            self.cell(col_width, header_height, heading, border=1, align="C", fill=True)
        self.ln()
        # Color and font restoration:
        self.set_text_color(black)
        self.set_font()
        week_num = 1
        for row in rows:

            if row[0].in_break:
                week_txt = ''
            else:
                week_txt = str(week_num)
                week_num += 1
            self.cell(week_col_width, col_height, week_txt, border='LRTB', align='C')
            for day in row:
                self.set_fill_color(day.bg)
                txt = str(day.number)
                if day.number == 1:
                    txt = day.month + ' 1'
                if day.in_break or day.weekdaynum > 5 or day.assign_weeks or day.is_holiday:  # break or a weekend
                    self.set_line_width(heavy_line_width)
                else:
                    self.set_line_width(normal_line_width)
                height = col_height
                # manually do the mult text lines
                # self.multi_cell will not work and self.write has bugs
                self.cell(col_width, height, '', border="LRTB", align="L", fill=True, new_y='TOP')
                first_bold = day.number == 1
                lines = [txt] + day.extras
                x, y = self.get_x(), self.get_y()
                l_height = height / 4
                line_x = x - col_width + 1
                line_y = y + 3

                for line in lines:
                    if first_bold:
                        self.set_font(style='B')
                        first_bold = False
                    else:
                        self.set_font()
                    self.text(line_x, line_y, line)
                    line_y += l_height

            self.set_line_width(normal_line_width)
            self.ln()


@dataclass
class Day:
    number: int
    weekdaynum: int
    month: str
    bg: int
    in_break: bool
    assign_weeks: bool
    extras: list[str]
    is_holiday: bool


def generate(s: Semester):
    pdf = PDF(orientation='portrait', format='A4', unit='mm')
    pdf.set_margin(5)
    pdf.add_page()

    pdf.set_font('helvetica', size=10)
    header = [x for x in calendar.day_name]
    rows = []
    curr_day = date(s.year, s.start_month, s.start_day)
    fill = False
    in_break = False
    assign_week = False
    term_week = 0
    for week in range(s.weeks_long):
        row = []
        if in_break and week + 1 == s.break_at_end_of_week + 3:
            in_break = False
        if not in_break:
            term_week += 1
        if term_week == s.assign_week_start:
            assign_week = True
        for day in range(7):
            if curr_day.day == 1:
                fill = not fill
            month_day = (curr_day.month, curr_day.day)
            bg = gray1 if fill else white
            if term_week == s.break_at_end_of_week and day == 5:
                in_break = True
            if in_break:
                bg = gray_break
            extras = s.due_dates[month_day]
            if month_day in s.holidays:
                extras = [s.holidays[month_day]]
                bg = holiday_gray

            d = Day(number=curr_day.day, weekdaynum=day + 1, month=calendar.month_name[curr_day.month], bg=bg,
                    assign_weeks=assign_week, in_break=in_break, extras=extras, is_holiday=month_day in s.holidays)
            row.append(d)
            curr_day += timedelta(1)
        rows.append(row)

    pdf.table(header, rows)
    pdf.output(f"timetable_{s.year}_{s.semester_name}.pdf")
