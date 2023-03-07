install.packages('ggbackground')
library(ggplot2)
library(ggbackground)

# 새로운 ggplot 생성
p <- ggplot(mtcars, aes(x = wt, y = mpg)) + 
  geom_point()

# 이미지 파일 경로 설정
img_path <- "path/to/image.png"

# 이미지를 ggplot에 추가
p <- p + add_background_image(img_path, alpha = 0.5)

# 결과 확인
library(ggimage)
install.packages('png')

install.packages('ggimage')
library(png)
library(grid)
img <- readPNG("korea.png")
ggplot() + 
  theme_void()+
  annotation_custom(rasterGrob(img), xmin=-Inf, xmax=Inf, ymin=-Inf, ymax=Inf)
