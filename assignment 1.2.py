{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Warmup Assignment 2\nBelow you see some ApacheSpark code written in Python. You don't have to change code now, the only thing we want you to do is to make sure that you have a proper Apache Spark Notebook environment available for this course\n\n"
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "Waiting for a Spark session to start...\nSpark Initialization Done! ApplicationId = app-20200127212208-0000\nKERNEL_ID = 1d1d8519-73bd-4ff1-a384-d01d12f455ff\n"
                }
            ],
            "source": "def assignment1(sc):\n    rdd = sc.parallelize(list(range(100)))\n    return rdd.count()"
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "100\n"
                }
            ],
            "source": "print(assignment1(sc))"
        },
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "--2020-01-27 21:22:18--  https://raw.githubusercontent.com/IBM/coursera/master/rklib.py\nResolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133\nConnecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.\nHTTP request sent, awaiting response... 200 OK\nLength: 2540 (2.5K) [text/plain]\nSaving to: 'rklib.py'\n\n100%[======================================>] 2,540       --.-K/s   in 0s      \n\n2020-01-27 21:22:18 (43.3 MB/s) - 'rklib.py' saved [2540/2540]\n\n"
                }
            ],
            "source": "!rm -f rklib.py\n!wget https://raw.githubusercontent.com/IBM/coursera/master/rklib.py"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Please provide your email address and obtain a submission token on the grader\u2019s submission page in coursera, then execute the cell"
        },
        {
            "cell_type": "code",
            "execution_count": 4,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "Submission successful, please check on the coursera grader page for the status\n-------------------------\n{\"elements\":[{\"itemId\":\"D277m\",\"id\":\"sUpST4RAEeawAApvKZgcCQ~D277m~NACft0FLEeqxAArxsrPvkw\",\"courseId\":\"sUpST4RAEeawAApvKZgcCQ\"}],\"paging\":{},\"linked\":{}}\n-------------------------\n"
                }
            ],
            "source": "from rklib import submit\nimport json\n\nkey = \"R1eDmiHNEei9kxIYdin0mA\"\npart = \"fnFg7\"\nemail = \"gbhatia880@gmail.com\"\ntoken = \"WO8SvvMLDCi8151F\"\n\nsubmit(email, token, key, part, [part], json.dumps(assignment1(sc)))"
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "<map at 0x7fa9ccb31c50>"
                    },
                    "execution_count": 2,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "def f(x):    \n  return (x+2)*2    \nl = [1,2,3,4]\nmap(f,l)"
        },
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "15"
                    },
                    "execution_count": 3,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "sc.parallelize([1,2,3,4,5]).reduce(lambda a,b:a+b)"
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": ""
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.6 with Spark",
            "language": "python3",
            "name": "python36"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.6.8"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 1
}