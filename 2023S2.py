import semcal

s = semcal.Semester(2023, 7, 17)

s.semester_name = 'S2'  # for generated filename
s.weeks_long = 19  # including mid-semester break
s.break_at_end_of_week = 10  # week before semester break

s.assign_week_start = 15  # week when assignment week begins. not including break weeks

s.holiday(10, 23, "Labour Day")

s.holiday(8, 16, 'Staff Engagement')

s.due(10, 22, 'PRJ Journal')
s.due(11, 5, "PRJ Report")
s.due(11, 9, "PRJ Poster")
s.due(11, 9, "Academic Adv.")
s.due(7, 20, 'PRJ Proposal')
s.due(8, 10, 'PRJ Talk prep')
s.due(8, 17, 'PRJ Seminar 1')
s.due(9, 21, 'PRJ Writing class')
s.due(10, 19, 'PRJ Seminar 2')
s.due(11, 2, 'PRJ Poster class')

s.due(9, 7, "OSA Test")
s.due(9, 19, 'OSA Assign 1')
s.due(11, 14, 'OSA Assign 2')

s.due(9, 7, 'NET Presentation')
s.due(9, 22, 'NET Journal 1')
s.due(9, 22, 'NET Tutorial')

s.due(11, 6, 'NET Journal 2')
s.due(11, 16, 'NET Report')

semcal.generate(s)
