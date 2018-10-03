.data
T: .word  0xABCDEF00
best_matching_score: .word -1 # best score = ? within [0, 32]
best_matching_Hamming: .word -1 # how many patterns achieve the best score?
Pattern_Array: .word 0, 1, 2, 3, 4, -1, -2, -3, -4, -5, 0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA, 0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999
Score_Array:   .word 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0


.text
    addi $15, $0, 0x2000    # start address of the data is stored in $15
    addi $17, $15, 0xC       # address of the array is stored in $17
    lw  $11, 0($15)          # pattern is loaded into $11
    lw  $10, 4($15)         # The current best matching score is loading into $10 from memory
    addi  $15, $0, 20       # numbers of words in the array
	
LoopWords:
    lw  $16, 0($17)          # Load a word from meory
    xor $16, $16, $11        # The xor will give us the information needed to count for the hamming distance
    add  $13, $0, $0        # We will be storing the hamming distance in $13, therefore, we load a 0
	
Hamming:    
    beq  $16, $0, endHamming
    andi $14, $16, 1        # With the handy andi, we get the most significant bit
	jal IncrementCount    
	
Next:        
    srl  $16, $16, 1        # We shift to compare with the next bit   
    j    Hamming              # Keep looping
	
endHamming:    
    addi $14, $0, 32
    sub $14, $14, $13       # Calculation of score
    
    slt $13, $14, $10       # If the score is lower than the best, we will not save it
    bne $13, $0, SkipSaving
    add $10, $0, $14        # If not: then current score will be saved as best score

SkipSaving:
    sw   $14, 80($17)        # Calculate direction is score array

    addi $17, $17, 4          # Move to the next position in the array
    addi $15, $15, -1       # We must do this for all words in the array
    bne  $15, $0, LoopWords

    addi $17, $0, 0x2004     
    sw   $10, 0($17)         # We save the best score in the given address

    addi $17, $0, 0x205C     # Here we save start address of score array in $
    addi $11, $0, 20         # We store the number of words in the array, usfeul for oops
    addi $15, $0, 0         # Counter of scores
	
LoopScores:
    lw   $16, 0($17)         # We load a score from array

    bne  $10, $16, NextStep   # If it is lower, then nothing will happen
    addi $15, $15, 1        # If they are equal, the score is incremented 
	
NextStep:
    addi $17, $17, 4          #advance to next array word
    addi $11, $11, -1         
    beq  $11, $0, EndOfProgram
	j LoopScores
IncrementCount:
	add  $13, $13, $14      # We add the result of the hamming count. If it's zero, then nothing happens
	jr $31
	
EndOfProgram:
	addi $17, $0, 0x2008     # We recover the given address to store result
    sw   $15, 0($17)         # the result is stored back into data	
