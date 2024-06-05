import semcal

s = semcal.Semester(2024, 6, 22, 'S2')

s.weeks_long = 18  # including mid-semester break
s.break_at_end_of_week = 10  # week before semester break

s.assign_week_start = 16

semcal.generate(s)
