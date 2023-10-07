async def calc_calories(kg, height, age, activity_hours):
    bom = 447.593 + (9.247 * kg) + (3.098 * height) - (4.330 * age)
    activity_coefficient = 1.4
    return (bom * activity_coefficient) / 24 * activity_hours
