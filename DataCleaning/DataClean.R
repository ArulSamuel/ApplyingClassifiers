dataInitial <- read.csv("ProjectData.csv",nrows=5)
classes <- sapply(dataInitial,class)
data <- read.csv('ProjectData.csv',colClasses=classes)
write.table(data, file="new.txt", sep=" ",col.names=FALSE,row.names=FALSE)
