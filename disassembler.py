# Disassembler for project 2
#This code works for both program 1 and 2

input_file = open("MachineCodeProgram1.txt", "r")
output_file = open("project2_group_15_p1_asm.txt", "w")

for line in input_file: 
    if(line[0:7] == "0000000"):
        output_file.write("add $8, $18,$0\n")
    elif(line[0:7] == "0000001"):
        output_file.write("add $10, $0, $8\n")
    elif(line[0:7] == "0000010"):
        output_file.write("add $10, $0, $14\n")
    elif(line[0:7] == "0000011"):
        output_file.write("add $10, $18, $0\n")
    elif(line[0:7] == "0000100"):
        output_file.write("add $13, $13, $14\n")
    elif(line[0:7] == "0000101"):
        output_file.write("add $13, $0, $0\n")
    elif(line[0:7] == "0000110"):
        output_file.write("add $13, $10, $0\n")
    elif(line[0:7] == "0000111"):
        output_file.write("add $14, $8, $0\n")
    elif(line[0:7] == "0001000"):
        output_file.write("add $14, $10, $0\n")
    elif(line[0:7] == "0001001"):
        output_file.write("add $18, $18, $14\n")
    elif(line[0:7] == "0001010"):
        output_file.write("addi $8, $0, 1\n")
    elif(line[0:7] == "0001011"):
        output_file.write("addi $10, $0, 6\n")
    elif(line[0:7] == "0001100"):
        output_file.wite("addi $11, $0, 20\n")
    elif(line[0:7] == "0001101"):
        output_file.write("addi $10, $10, -17\n")
    elif(line[0:7] == "0001110"):
        output_file.write("addi $11, $11, -1\n")
    elif(line[0:7] == "0001111"):
        output_file.write("addi $12, $0, 0x2000\n")
    elif(line[0:7] == "0010000"):
        output_file.write("addi $12, $0, 17\n")
    elif(line[0:7] == "0010001"):
        output_file.write("addi $13, $13, -1\n")
    elif(line[0:7] == "0010010"):
        output_file.write("addi $14, $0, 32\n")
    elif(line[0:7] == "0010011"):
        output_file.write("addi $15, $0, 0x2000\n")
    elif(line[0:7] == "0010100"):
        output_file.write("addi $15, $0, 0x2004\n")
    elif(line[0:7] == "0010101"):
        output_file.write("addi $15, $0, 20\n")
    elif(line[0:7] == "0010110"):
        output_file.write("addi $15, $15, -1\n")
    elif(line[0:7] == "0010111"):
        output_file.write("addi $15, $0, 0\n")
    elif(line[0:7] == "0011000"):
        output_file.write("addi $15, $15, 1\n")
    elif(line[0:7] == "0011001"):
        output_file.write("addi $17, $17, 4\n")
    elif(line[0:7] == "0011010"):
        output_file.write("addi $17, $15, 0xC\n")
    elif(line[0:7] == "0011011"):
        output_file.write("addi $17, $17, 4\n")
    elif(line[0:7] == "0011100"):
        output_file.write("addi $17, $0, 0x2004\n")
    elif(line[0:7] == "0011101"):
        output_file.write("addi $17, $0, 0x205C\n")
    elif(line[0:7] == "0011110"):
        output_file.write("addi $17, $0, 0x2008\n")
    elif(line[0:7] == "0011111"):
        output_file.write("addi $18, $0, 0\n")
    elif(line[0:7] == "0100000"):
        output_file.write("andi $11, $15, 1\n")
    elif(line[0:7] == "0100001"):
        output_file.write("andi $14, $16, 1\n")
    elif(line[0:7] == "0100010"):
        output_file.write("beq  $11, $0, Continue\n")
    elif(line[0:7] == "0100011"):
        output_file.write("beq  $11, $0, EndOfProgram\n")
    elif(line[0:7] == "0100100"):
        output_file.write("beq  $13, $0, ReturnToPrevious\n")
    elif(line[0:7] == "0100101"):
        output_file.write("beq  $14, $0, ReturnToPrevious\n")
    elif(line[0:7] == "0100110"):
        output_file.write("beq  $15, $0, ExponentZero\n")
    elif(line[0:7] == "0100111"):
        output_file.write("beq  $16, $0, endHamming\n")
    elif(line[0:7] == "0101000"):
        output_file.write("bne $11, $0, ReturnToPrevious\n")
    elif(line[0:7] == "0101001"):
        output_file.write("bne $13, $0, SkipSaving\n")
    elif(line[0:7] == "0101010"):
        output_file.write("bne $15, $0, LoopWords\n")
    elif(line[0:7] == "0101011"):
        output_file.write("bne $10, $16, NextStep\n")
    elif(line[0:7] == "0101100"):
        output_file.write("j MainLoop\n")
    elif(line[0:7] == "0101101"):
        output_file.write("j SecondaryLoop\n")
    elif(line[0:7] == "0101110"):
        output_file.write("j EXIT\n")
    elif(line[0:7] == "0101111"):
        output_file.write("j Modulus\n")
    elif(line[0:7] == "0110000"):
        output_file.write("j Hamming\n")
    elif(line[0:7] == "0110001"):
        output_file.write("j LoopScores\n")
    elif(line[0:7] == "0110010"):
        output_file.write("jal Multiplication\n")
    elif(line[0:7] == "0110011"):
        output_file.write("jal Modulus\n")
    elif(line[0:7]== "0110100"):
        output_file.write("jal IncrementCount\n")
    elif(line[0:7]== "0110101"):
        output_file.write("jr  $31\n")
    elif(line[0:7]== "0110110"):
        output_file.write("lw  $10, 4($15)\n")
    elif(line[0:7]== "0110111"):
        output_file.write("lw  $11, 0($15)\n")
    elif(line[0:7]== "0111000"):
        output_file.write("lw  $15, 0($12)\n")
    elif(line[0:7]== "0111001"):
        output_file.write("lw  $16, 0($17)\n")
    elif(line[0:7]== "0111010"):
        output_file.write("slt $11, $10, $12\n")
    elif(line[0:7]== "0111011"):
        output_file.write("slt $13, $14, $10\n")
    elif(line[0:7]== "0111100"):
        output_file.write("srl $15, $15, 1\n")
    elif(line[0:7]=="0111101"):
        output_file.write("srl $16, $16, 1\n")
    elif(line[0:7]=="0111110"):
        output_file.write("sub $14, $14, $13\n")
    elif(line[0:7]=="0111111"):
        output_file.write("sw  $8, 4($12)\n")
    elif(line[0:7]=="1000000"):
        output_file.write("sw  $10, 0($17)\n")
    elif(line[0:7]=="1000001"):
        output_file.write("sw  $10, 0($15)\n")
    elif(line[0:7]== "1000010"):
        output_file.write("sw  $14, 80($17)\n")
    elif(line[0:7]== "1000011"):
        output_file.write("sw  $15, 0($17)\n")
    elif(line[0:7]== "1000100"):
        output_file.write("xor $16, $16, $11\n")



        


        
