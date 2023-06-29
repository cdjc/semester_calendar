import semcal

s = semcal.Semester(2023, 2, 20)

s.semester_name = 'S1'  # for generated filename
s.weeks_long = 19  # including mid-semester break
s.break_at_end_of_week = 7  # week before semester break

s.assign_week_start = 15

s.due(6, 22, 'NET Demo')
s.due(2, 26, 'PRJ Proposal')
s.due(5, 28, 'PRJ Journal')
s.due(6, 11, 'PRJ report')
s.due(6, 15, 'PRJ poster')
s.due(6, 15, 'Academic Adv.')

s.due(6, 18, 'SYD Assign 2')
s.due(6, 4, 'SYD Journal')
s.due(4, 6, 'SYD Assign 1')

s.due(6, 18, 'RES Assign 2')
s.due(6, 4, 'RES Journal')
s.due(4, 30, 'RES Assign 1')

s.due(4, 6, 'NET Test')
s.due(6, 11, 'NET Assign')

s.holiday(4, 10, 'Easter')
s.holiday(4, 25, 'ANZAC')
s.holiday(4, 7, 'Easter')
s.holiday(6, 5, "King's Birthday")

semcal.generate(s)
