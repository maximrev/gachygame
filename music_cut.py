
from pydub import AudioSegment

song = AudioSegment.from_mp3("music/Junost_v_sapogah.mp3")

startMin = 0
startSec = 8.3	# 0 to 60

endMin = 0
endSec = 8.7	# 0 to 60
file_name = str(startMin) + str(startSec) + '_' + str(endMin) + str(endSec)

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment
extract = song[startTime:endTime]

# Saving
extract.export('music/' + file_name + '.mp3', format="mp3")
