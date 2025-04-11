def get_zodiac_sign(day, month):
    """
    Determines the zodiac sign based on the day and month.

    Args:
        day (int): The day of the month (1-31).
        month (int): The month of the year (1-12).

    Returns:
        tuple: A tuple containing the zodiac sign name (str) and a brief characteristic (str),
               or None if the date is invalid.
    """
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return None, "Invalid date."

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", "Energetic, courageous, and often impulsive."
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", "Patient, reliable, and enjoys comfort."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", "Curious, adaptable, and communicative."
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", "Nurturing, sensitive, and family-oriented."
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", "Confident, passionate, and natural leaders."
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", "Analytical, practical, and detail-oriented."
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", "Balanced, fair, and seeks harmony."
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", "Intense, determined, and often mysterious."
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", "Optimistic, adventurous, and loves freedom."
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", "Disciplined, ambitious, and responsible."
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", "Independent, innovative, and humanitarian."
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces", "Compassionate, artistic, and intuitive."
    else:
        return None, "Invalid date."

if __name__ == "__main__":
    while True:
        try:
            day = int(input("Enter the day of the month (1-31): "))
            month = int(input("Enter the month (1-12): "))
            zodiac_sign, characteristic = get_zodiac_sign(day, month)
            if zodiac_sign:
                print(f"Your zodiac sign is {zodiac_sign}.")
                print(f"Characteristic: {characteristic}")
            else:
                print(characteristic)
            break
        except ValueError:
            print("Invalid input. Please enter numbers for the day and month.")
