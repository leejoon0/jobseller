def save_to_file(file_name, keywords):
    file = open(f"{file_name}.csv", "w")
    file.write("키워드,월간검색수(PC),월간검색수(모바일)\n")
    for k in keywords:
        file.write(f"{k['keyword']},{k['monthlySrhCountPC']},{k['monthlySrhCountMobile']}\n")

    file.close()