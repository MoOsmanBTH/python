def multiplication_table(file_name, integer):
    table = open(file_name, "w+")
    for i in range(1, integer, 1):
        for j in range(1, integer, 1):
            table.write("%d " % (i * j))
        table.write("\n")
    table.close()
    
multiplication_table("Multiplation_table.txt", 10)