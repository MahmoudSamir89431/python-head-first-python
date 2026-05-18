import statistics
FOLDER = "swimdata/"
def read_swim_data(filename):

    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")


    with    open(FOLDER + filename) as file:
        lines = file.readlines()

    times = lines[0].strip().split(",")
    converts = []
    for t in times:

    #extract the component parts: start with minute value
        minutes, rest = t.split(":")
        seconds, hundrenths = rest.split(".")

    #convert strings to numbers
        converted_time = (int(minutes) *60 *100) + (int(seconds) * 100) + int(hundrenths)

    #display result
        converts.append(converted_time)


    average = statistics.mean(converts)
    mins_secs, hundrenths = str(round(average / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes*60
    average = str(minutes) + ":" +str(seconds)+ "." + hundrenths
    return swimmer, age, distance, stroke, times, average