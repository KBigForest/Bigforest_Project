setwd('C:/Users/dddf/Desktop/gdp')
gdp <- read.csv('gdp.csv',header = T)
colnames(gdp) <- c('year','gdp', 'Birth','Death','Merry','Divorce','Working')
gdp <- gdp[,-1]
gdp <- gdp[c(-1,-3),]
gdp
library(psych)
summary(gdp)
plot(gdp$year,gdp$Birth,type ='o',ylim = c(200000,1000000))
library(ggplot2)
library(tidyverse)
library(dplyr)
install.packages('tidyverse')

gdp <- read.csv('gdp.csv',header = T)
colnames(gdp) <- c('year','gdp', 'Birth','Death','Merry','Divorce','Working')
gdp
gdp %>%
  ggplot(aes(x = year, y = Birth)) +
  geom_line()+
  geom_point()+
  scale_y_continuous(name ='출생자 수',labels = scales::comma)+
  scale_x_continuous(name ='연도')+
  labs(title = '연도별 출생자 수', 
       title.size = 50)+
  annotate("text", x = 1980, y = max(gdp$Birth), label = "86만", size = 6)+
  annotate("text", x = 2022, y = min(gdp$Birth), label = "25만", size = 6)
#    theme(axis.title = element_text(size=30),
#        title = element_text(size=40))

  makingboxplot <- function(data){
  q1 <- quantile(data, 0.25)
  q3 <- quantile(data, 0.75)
  iqr <- q3 - q1
  threshold <- 1.5 * iqr
  lower <- q1 - threshold
  upper <- q3 + threshold
  outliers_tukey <- data[data < lower | data > upper]
  boxplot(data, ylim = c(min(data), max(data) * 1.1))
  points(outliers_tukey, col = "red", pch = 16)
}

par(mfrow=c(2,3))
for (i in 3:7){
  makingboxplot(gdp[,i])
}
pairs.panels(gdp)

gdp
dat1 <- gdp
sum(is.na(dat1))















dat1$gdp
gdp <- read.csv('gdp.csv',header = T)
colnames(gdp) <- c('year','gdp', 'Birth','Death','Merry','Divorce','Working')
model1 <- lm(gdp ~ Birth+Death+Merry+Divorce+Working, data = dat1)
summary(model1)
model2 <- lm(gdp ~ Merry+Divorce+Working, data = dat1)
summary(model2)
plot(model2,1)
plot(model2,2)
plot(model2,3)
plot(model2,4)
gvlma(model2)

model3 <- lm(log(gdp) ~+log(Merry)+log(Working), data = dat1)
summary(model3)
gvlma(model3)

plot(model3,1)
plot(model3,2)
plot(model3,3)
plot(model3,4)


#10이넘으면 다중공선성 존재한다고 판단
par(mfrow=c(1,1))
plot(model2,1)
shapiro.test(model2$residuals)
model2 <- lm(gdp ~ Merry+Divorce+Working, data = dat1)
summary(model2)
plot(model2,4)
#정규성 가지고 있음
#등분산성 O

plot(model2,4)
install.packages('olsrr')
library(olsrr)
ols_plot_cooksd_bar(model2)
both <- step(model1, direction = "both", trace = F)
both

library(MASS)
model4<- lm(Birth~Merry+Working, data= gdp)
summary(model4)
plot(model4,4)
step.forward = stepAIC(model2,                             # 절편만 있는 모형에서 시작
                       direction = "both")
