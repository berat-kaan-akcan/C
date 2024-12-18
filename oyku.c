#include <stdio.h>

int main() {
    printf("Hello, Mars!\n");

    return 0;
}


#include <stdio.h>


int main (){
 
    
    //int number1 = 10;
    //int number2 = 2;
    

    //int number1 = 10, number2 = 2;
    
    
    int number1 = 10, number2 = 2;


    int sum = number1 + number2;
    int modulo = number1 % number2;

    printf("Summation : %d, and Modulo: %d\n", sum, modulo);
    printf("Adress int: %d \n", &sum);
    printf("Adress hex: %x \n", &sum);

    

    
    int number1, number2 ;
    
    //printf("Number 1 : %d \n", number1);
    //printf("Number 2 : %d\n", number2);

    printf("Please give me number1: ");
    scanf("%d" ,&number1);
    printf("Please give me number2: ");
    scanf("%d" ,&number2);

    int sum = number1 + number2;
    int mod = number1 % number2;

    printf("Summation : %d, and Modulo : %d\n", sum, mod);
    
    
    
    // CHAPTER 3
    
    int a = 5;
    printf("%d\n", a);
    int b = a++;
    printf("a: %d, b: %d\n", a, b);
    int c = ++a;
    printf("a: %d\n", a);
    printf("b: %d\n", b);
    printf("c: %d\n", c);

    //int a = 5;
    //printf("a: %d\n", a);
    //int b = a++;
    //printf("b: %d\n", b);
    //int c = ++a;
    //printf("c: %d\n", c);
    


   for(int myVar = 0; myVar <= 10; myVar++){
        printf("myVar is: %d\n", myVar);
        printf("myVar is: %d\n", myVar);
    }
    // one statement var ise süslü parantez kullanmadan yazabilirim (yukarda tek satır printf olunca mesela)
    // ilk myVar'ı for loop'un içinde kabul eder diğerini etmez


    int age = 20;
    printf("Please give me the age: ");
    scanf("%d", &age);

    if (age >= 18){
        printf("You are an adult.\n");
    }
    else if (age < 16){
        printf("You cannot get moto DL.\n");
    }
    else {
        printf("You are a minor.\n");
    }
    
    int myVar = 0;
    while(myVar < 10) {
        if(myVar % 2 == 1){
        printf("myVar : %d\n", myVar);
        }else{
            break;
        }
        myVar++;
    }
    printf("myVar : %d\n", myVar);

    
    return 0;
}




#include <stdio.h>

int main(){

    /// sınav
    char x = 'a';
    if(x = 31){
        printf("true\n");
    }
    else{
        printf("false\n");
    }


    return 0;
}





#include <stdio.h>
// python'a çevir

int factorialFor(int number);
int factorialWhile(int number);
int factorialRecursive(int number); //loop yok, içerde değişken tanımlanmaz , //base case

int main(){

    int factorial_5 = factorialFor(5);
    printf("faktorial %d\n", factorial_5);
    int factorial_6 = factorialWhile(6);
    printf("faktorial %d\n", factorial_6);
    int factorial_7 = factorialRecursive(7);
    printf("factorial %d\n", factorial_7);
   
    int fibonacci = fibonacciFor(7);
    printf("fibonacci %d\n", fibonacci);
    int fibonacci_o = fibonacciWhile(7);
    printf("fibonacci %d\n", fibonacci_o);
    int fibonacci_r = fibonacciRecursive(7);
    printf("fibonacci %d\n", fibonacci_r);
    
    return 0;

}

int factorialFor(int number){
    
    if(number < 0){
        return 0;
    }
    if(number == 0){
        return 1;
    }
    int result = 1;
    for (int i = 1; i <= number; i++){
        result = result * i;

    }
    return result;
}

int factorialWhile(int number){

    int result = 1;
    while(number > 0){
        result *= number;
        number --;
        if(number == 1){
            break;
        }
    }
    return result;
}

int factorialRecursive(int number){
    //Base Case
    if(number == 1 || number == 0){
        return 1;
    }
    return number * factorialRecursive(number - 1);
    
}

int fibonacciFor(int number){

   int first_num = 1;
   int second_num = 1;
   int result = 0;
   if(number == 1 || number == 2){
        return 1;
    }
    for(int i = 3; i <= number; i++){
        result = first_num + second_num;
        first_num = second_num;
        second_num = result;
    }
    return result;

}

int fibonacciWhile(int number){ 

    int a = 1, b = 1, result = 0;
    if(number == 1 || number == 2){
        return 1;
    }

    while(number >= 3){
        result = a + b;
        a = b;
        b = result;
        number--;

    } return result;

}

// bilgisayar sonsuz döngüyü anlayamıyor 

int fibonacciRecursive(int number){

    //Base Case
    if(number == 1 || number == 2){
        return 1;
    }
    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2);
    
}




#include <stdio.h>
int main(){
    
    int i = 0;

    while(i < 5){
        printf("%d\n", i);
        i++;
    }

    do{ //quiz - sınavda çıkar (bununla yaptığımı if ile de yapabilirim)
        printf("%d\n", i);
        i++;

    }while(i < 5);

    //switch case de çok kullanılmaz (do-while gibi)
    //switch casedeki breakin kaldırılması
    //primitive (int,char,float,double - bool yok)
    //array'lerde aynı type olmalı

    int numbers[5] = {1,2,3,4,5,6};


    return 0;
}








#include <stdio.h>
// notion üni vize soruları (array quiz)
// satranç oyunu (matrix)

void myAppend(int array[], int size, int element);
void PrettyPrint(int array[], int size);
void Square(int num1, int num2);

int main(){

    int myArray[10];
    int myMatrıx[3][4];

    int myMatrıs[3][3]= {{1,2,3},{4,5,6},{7,8,9}};

    myArray[5] = 5; //5. indexe 5'i koyduk

    for(int i = 0; i < 10; i++){
        printf("%d\n", myArray[i]);
    }

    for(int a = 0; a < 3; a++){
        printf("%d\n", myMatrıx[a][0]);
    }


    for(int b = 0; b < 3; b++){
        for(int c = 0; c < 3; c++){
            if(c == 2){
                printf("%d", myMatrıs[b][c]);
            }else{
                printf("%d, ", myMatrıs[b][c]);
            }
            
        }printf("\n");
    }



    int example[10] = {}; //empty array
    for(int i = 0; i<10; i++){
        printf("%d\n", example[i]); //bütün elementlerim sıfır
    }

    for(int i = 1; i<15; i++){
        myAppend(example,10,i);
        PrettyPrint(example,10);
    }

    Square(1,100);


    return 0;
}

void myAppend(int array[], int size, int element){

    for(int i = 0; i < size; i++){
        if(array[i] == 0){
            array[i] = element;
            break;
        }
    }

    int sizeof array[] = size;

    if(element>0){
        array[0] = element;

    }else{

    }

}

void PrettyPrint(int array[], int size){
    
    for(int i = 0; i < size; i++){
        printf("%d ", array[i]);
    }printf("\n");

}
//eğer karekökten çıkabiliyorsa yazsın
void Square(int num1, int num2){

    for(int i = num1; i < num2; i++){ //benim doğrum
        for(int j = num1; j < num2; j++){
             if(i == j*j){
                printf("%d\n", i);
            }else{
                continue;
            }
        }
    }

    for(int i = num1; i < num2; i++){ //yanlış
        if(i*i <= num2){
            printf("%d", i*i);
        }
    }

    for(int i = num1; i < num2; i++){ //doğru
        if(i*i >= num1 && i*i <= num2){
            printf("%d", i*i);
        }
    }

    for(int i = num1; i*i < num2; i++){ //daha doğru
        if(i*i >= num1){
            printf("%d", i*i);
        }
    }

    //optimizasyon yaptık kodumuza

}