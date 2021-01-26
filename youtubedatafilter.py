video_info = open("youtubedata.txt", "r")

content_list = ["".join(line.strip()) for line in video_info if line.startswith("Watched")]

print("\n".join(content_list))

video_info.close()
