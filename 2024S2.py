import semcal

s = semcal.Semester(2024, 7, 22, 'S2')

s.weeks_long = 17  # including mid-semester break
s.break_at_end_of_week = 10  # week before semester break

s.assign_week_start = 14

s.holiday(10, 28, "Labour Day")

# PRJ assessments and classes
s.due(11, 7, "PRJ Poster")
s.due(11, 3, "PRJ Report")
s.due(10, 20, "PRJ Journal")

s.due(7, 25, 'PRJ Proposal')
s.due(8, 8, 'PRJ Talk prep')
s.due(8, 15, 'PRJ Seminar 1')
s.due(9, 26, 'PRJ Writing class')
s.due(10, 24, 'PRJ Seminar 2')
s.due(10, 31, 'PRJ Poster class')


s.due(10, 23, "SYD A1 Journal")
s.due(9, 11, 'SYD A2 Failed')
s.due(11, 6, 'SYD A3 Design')

s.due(9, 5, "OSA Test")
s.due(9, 19, 'OSA CompPrep')
s.due(11, 13, 'OSA A3 Demo')

s.due(9, 6, 'NET Presentation')
s.due(9, 20, 'NET Journal 1')
s.due(9, 20, 'NET Tutorial')

s.due(11, 8, 'NET Report')

semcal.generate(s)
