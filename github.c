/*  
gcc hello.c -o hello
./hello
nano hello.c

*/







// include <stdio.h>

// int main() {
//     printf("Hello, World!\n");
//     return 0;
// }


#include <stdio.h>

int main (){
    /*
    //int number1 = 10 ,int number2 = 2;
    
    int number1 = 10 , number2 = 2;
    
    int sum = number1 + number2;

    int modulo = number1 % number2;

    printf("Summation : %d, and Modulo : %d\n",sum,modulo);
    printf("Adress : %d\n ", &sum);
    printf("Adress : %X\n ", &sum);
    return 0;
    */

    /*
    int number1 , number2 ;
    printf("please give me Number 1 :  ");
    scanf("%d" , &number1);
    printf("Please give me Number 2 :  ");
    scanf("%d" , &number2);
    
    int sum = number1 + number2;
    int mod = number1 & number2;
    printf("Summation : %d, and Modulo : %d\n" ,sum ,mod);

    */
    
    // int a = 5; 
    // int b = a++;
    // int c = ++a;
    // printf("a: %d\n ", a);
    // printf("b: %d\n ", b);
    // printf("c: %d\n ", c);
    
    // for(int myVar = 0; myVar <=10; myVar++){
    //     printf("MyVar is : %d\n ", myVar);
    //     printf("MyVar is : %d\n ", myVar);}
    
    // int age ;
    // printf("please give me the age : ");
    // scanf("%d", &age );
    // if (age >= 18) {
    //     printf("You are an adult.\n");}
    // else if (age < 16){
    //     printf("you cannot moto dl .\n ");
    // }else{ ""
    //     printf("You are a minor.\n");
    
    // }

    // int myVar = 0;
    // while(myVar < 10 ){
    //     if(myVar % 2 == 1){
    //         printf("myvar : %d " ,myVar);
    //     }else {
    //         break;
    //     }

    //     myVar++;
    // }
    // printf("myvar : %d " ,myVar);
        

    // return 0;
return 0;
}



/*
int factorial(int number);
int factorialFor(int number);
int factorialWhile(int number);
int factorialRecursive(int number);
int fibonacciFor(int number);
int fibonacciWhile(int number);
int fibonacciRecursive(int number);
int main(){

    int factorial_5 = factorial(5);
    printf("Factorial %d\n",factorial_5);
    
    int factorial_5_for = factorialFor(5);
    printf("Factorial of 5 : %d\n",factorial_5_for);

    int factorial_5_while = factorialWhile(5);
    printf("Factorial of 5 : %d\n",factorial_5_while);

    int factorial_5_recursive = factorialRecursive(5);
    printf("Factorial of 5 : %d\n",factorial_5_recursive);

    int fibonacci_10_for = fibonacciFor(10);
    printf("Fibonacci of 10 : %d\n",fibonacci_10_for);

    int fibonacci_10_while = fibonacciWhile(10);
    printf("Fibonacci of 10 : %d\n",fibonacci_10_while);

    int fibonacci_10_Recursive = fibonacciRecursive(10);
    printf("Fibonacci of 10 : %d\n",fibonacci_10_Recursive);
    





    return 0;
}

int factorial(int number) {
    return factorialFor(number);
}


int factorialFor(int number){
    int  result = 1;
    for (int i = 1; i <= number ; i++){
        result *= i;
    }
    return result;
}   

int factorialWhile(int number){
    if(number<0){

    }
    if(number == 0){
        return 0;
    }
    int result = 1;
    while(number > 0){
        result = result * number;
        number--;

    }

}




int factorialRecursive(int number){
    //base case
    if(number == 1 || number == 0){
        return 1;
    }

    return number*factorialRecursive(number -1);

}



int fibonacciFor(int number){
    int first = 1, second = 1, result = 1;
    if(number == 1 || number == 2){
        return 1;
    }
    for(int i = 3; i <= number; i++){
        result=first+ second;
        first=second;
        second=result;
    }
    return result;
}

int fibonacciWhile(int number){
    int first = 1, second = 1, result = 1;
    if(number == 1 || number == 2){
        return 1;
    }
    int count = 3;
    while(count <= number){
        result=first+second;
        first=second;
        second=result;
        count++;
    }
    return result;
}

int fibonacciRecursive(int number){
    //base case
    if(number == 1 || number == 2){
        return 1;
    }
    return fibonacciRecursive(number -1) + fibonacciRecursive(number-2);

}



#include <stdio.h>

int main(){
    int i = 0;
     
    while(i<5);
        printf("%d\n",i);
        i++;









    return 0;
}
 

#include <stdio.h>

int main(){
    int day  = 3;
    switch (day)
    {
    case 1 :
        printf("monday\n");
        
          
        
        break;
    case 2:
        printf("tuesday\n");
        break;

    case 3 :
        printf("wednesday\n");
        break;
    default:
        printf("invalid day\n");
        break;
    }






    return 0;
}
*/

#include <stdio.h>
#include <math.h>
/*
void Appendfunction(int array[],int size,int element);
void prettyPrint(int array[],int size);
*/
void function(int number1,int number2);

int main(){
    /*
    int myArray[10];

    
    myArray[5] = 5;
    for (int i = 0; i<10 ; i++){
        printf("%d\n",myArray[i]);
    }
    
    int multiArray[3][4];
    for ( int i = 0; i<3 ; i++){
        printf("%d\n",multiArray[i][0]);
    }
    
    

    int myArray[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    for(int i = 0; i<3; i++){
        for (int j = 0; j<3; j++){
            if(j == 2){
                printf("%d ",myArray[i][j]);

            }
            else{
                printf("%d, ",myArray[i][j]);

            }
            
            
        }
        printf("\n");
    }
    

    int example[10]={};
    for (int i = 0; i < 15 ; i++){
        
        Appendfunction(example,10,i);
        prettyPrint(example,10);
        

    }
     */
    function(2,90);










    return 0;
}
/*
void Appendfunction(int array[],int size,int element){

    for (int i = 0; i<size ; i++){

        if(array[i]==0){
            array[i] = element;
            break;
        }
    }


}

void prettyPrint(int array[],int size){
    for(int i = 0 ; i<size;i++){
        printf("%d",array[i]);
    }
    printf("\n");
}

*/
#include <math.h>
void function(int number1,int number2){
    for (int i=0; i*i<number2;i++){

        if(i*i>=number1){
            //printf("%d\n",i*i);
        }
        printf("%d ",i);


    }

}


merhaba 



