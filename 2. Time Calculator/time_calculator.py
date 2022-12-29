def timeFormatConvert(time, version = "24"):
  
  #This function was done with help from the article
  #https://www.freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock/
  
  if version == "24":
    timeDetails = time.split()
    hourComponent = int(timeDetails[0].split(":")[0])
    minuteComponent = int(timeDetails[0].split(":")[1])

    #if the input time is AM
    if timeDetails[1].lower() == "am":
      
      #if we are at midnight, transform 12 to 00
      if hourComponent == 12:
        return "00:" + str(minuteComponent).zfill(2)
      
      #if we are in AM and not at midnight, return the time as it is
      return timeDetails[0]
    
    #if the input is PM, the above will not end the function

    #if we are at midday, return the time as it is
    if hourComponent == 12:
      return timeDetails[0]
    
    return str(hourComponent + 12) + ":" + str(minuteComponent).zfill(2)
  else:
    hourComponent = int(time.split(":")[0])
    minuteComponent = int(time.split(":")[1])

    if hourComponent == 0:
      return "12:" + str(minuteComponent).zfill(2) + " AM"
    elif hourComponent == 12:
      return "12:" + str(minuteComponent).zfill(2) + " PM"
    elif hourComponent < 12:
      return str(hourComponent) + ":" + str(minuteComponent).zfill(2) + " AM"
    else:
      return str(hourComponent - 12) + ":" + str(minuteComponent).zfill(2) + " PM"

def weekDay(day):
  day = str(day).capitalize()

  if day == "0" or day == "Monday":
    return (0, "Monday")
  elif day == "1" or day == "Tuesday":
    return (1, "Tuesday")
  elif day == "2" or day == "Wednesday":
    return (2, "Wednesday")
  elif day == "3" or day == "Thursday":
    return (3, "Thursday")
  elif day == "4" or day == "Friday":
    return (4, "Friday")
  elif day == "5" or day == "Saturday":
    return (5, "Saturday")
  elif day == "6" or day == "Sunday":
    return (6, "Sunday")

def add_time(start, duration, day = ""):

  #convert the start time to 24h format
  start_24 = timeFormatConvert(start)

  start_24_hour = int(start_24.split(":")[0])
  start_24_minutes = int(start_24.split(":")[1])

  duration_hour = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])

  final_hour = start_24_hour + duration_hour
  final_minutes = start_24_minutes + duration_minutes

  if final_minutes > 59:
    final_minutes -= 60
    final_hour += 1

  numberOfDays = final_hour // 24
  new_time_hour = final_hour % 24
  new_time_minutes = final_minutes

  new_time = timeFormatConvert(str(new_time_hour) + ":" + str(new_time_minutes), "12")

  #if the day was provided
  if len(day) > 0:
    new_day = weekDay((weekDay(day)[0] + numberOfDays) % 7)[1]
    new_time = new_time + ", " + new_day
  
  if numberOfDays == 1:
    new_time = new_time + " (next day)"
  elif numberOfDays > 1:
    new_time = new_time + " (" + str(numberOfDays) + " days later)"
    
  return new_time