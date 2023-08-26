# print("麻黃是一味中藥，它的性味是辛、微苦，溫。而其歸經是肺膀胱，麻黃的功效是發汗解表，宣肺平喘，利水消腫。其應用為\n\t1.用於風寒表實證  \n\t2.用於咳喘實證  \n\t3.用於風水水腫。麻黃不適用的情況有: 體力差_體質虛弱、氣虛、自汗、大汗出、高血壓、高血壓_舒張壓高、血壓高低起伏變化、心臟麻痺、冠心病、心臟功能不全、心衰、心臟痛、心臟瓣膜病、二尖瓣脫垂、病態竇房結綜合征、心内膜炎、心臟性喘息、心臟肥大、心肌梗塞、狹心症、動脈硬化、病症嚴重、衰老_老年 ")


print("\t1. 实施强制的车辆排放标准和基于激励的计划askldjfhkasjdhfkljahsdfkljhaskldjfhksadhfklsahdfklahsdfkljhaskdlfjhksaldhfklasjdhfklsajhdflkjashdfkljhsadklfjhsakldjfhklasjdhfkljsahdfkljhasdklfjhsakldfjhkslajhdfklasjdhfklsajdhfklh，以降低车辆的碳足迹。\n\t2. 增加公共交通工具，减少公众对车辆的依赖。\n\t3. 增加对空气污染的影响的认识，鼓励市民减少污染物的生成。\n\t.4 投资于可再生能源的研究和开发，如太阳能和风能。\n\t5. 在工厂和发电厂安装空气污染控制装置，例如洗涤器。\n\t6. 对车辆和工厂使用清洁燃料。\n\t7. 实施更好的城市规划和控制拓展。\n\t8. 改善农业效率，减少化肥和杀虫剂的使用。\n9. 种植更多的树木以减少空气污染。\n10. 减少木材、煤炭和生物质的燃烧。")

# how do i modify regular expressoi nso that in the text :"其應用為1.用於風寒表實證 2.用於咳喘實證 3.用於風水水腫。麻黃不適用的情況 1.外感風熱，發熱無汗證，2.麻疹透發不暢，風疹瘙癢，3.水腫，小便不利"  the 1. 2. and 3. get detected and the text after the numebrs.  how do i modify regex =  r"(\d+\.\s*)(.*?)(\s|[。]{1})(?=\d+\.\s*|$)" to get that ?
# 其應用為1.用於風寒表實證 2.用於咳喘實證 3.用於風水水腫。麻黃不適用的情況
# 1.外感風熱，發熱無汗證，2.麻疹透發不暢，風疹瘙癢，3.水腫，小便不利