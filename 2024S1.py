import semcal

s = semcal.Semester(2024, 2, 19)

s.semester_name = 'S1'  # for generated filename
s.weeks_long = 19  # including mid-semester break
s.break_at_end_of_week = 8  # week before semester break

s.assign_week_start = 15

s.due(2, 19, "2024 S1")

# s.due(6, 22, 'NET Demo')
# s.due(2, 26, 'PRJ Proposal')
# s.due(5, 28, 'PRJ Journal')
# s.due(6, 11, 'PRJ report')
# s.due(6, 15, 'PRJ poster')
# s.due(6, 15, 'Academic Adv.')
#
# s.due(6, 18, 'SYD Assign 2')
# s.due(6, 4, 'SYD Journal')
# s.due(4, 6, 'SYD Assign 1')

s.due(3,15,"COM Assess 1")
s.due(4,12,"COM Assess 2")
s.due(6,14,"COM Assess 3")
#
s.due(4, 30, 'RES Assign 1')
s.due(6, 7, 'RES Journal')
s.due(6, 18, 'RES Assign 2')
#
s.due(4, 8, 'NET Test')  # Monday before break
s.due(6, 7, 'NET Assign')
s.due(6, 20, 'NET Demo')
#

s.holiday(3, 29, 'Easter Friday')
s.holiday(4, 1, 'Easter Monday')
s.holiday(4, 2, 'Easter Bonus')
s.holiday(4, 25, 'ANZAC')
s.holiday(6, 3, "King's Birthday")

semcal.generate(s)
