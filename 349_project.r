 setwd("/Users/Marcus/Desktop")
 fulldata = read.csv("2015-2016.csv")
 partialdata = read.csv("2015-2016_del.csv")
 fulldata = fulldata[,-1]
 partialdata = partialdata[,-1]
 result = fulldata[1] == 'W'
 result = result * 1
 fulldata = fulldata[,-1]
 partialdata = partialdata[,-1]
 fulldata = cbind(result,fulldata)
 partialdata = cbind(result,partialdata)
 cor_f = cor(fulldata[,2:41])
 cor_p = cor(partialdata[,2:27])
 cor_f = cor_f > 0.7
 cor_p = cor_p > 0.7
 cor_f = cor_f * 1
 cor_p = cor_p * 1