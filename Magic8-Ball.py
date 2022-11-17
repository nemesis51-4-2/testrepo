{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5740490-0781-4801-b203-a534c5b85b14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Magic 8-Ball Simulator.\n",
      "Ask me a Yes or No Question.\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def response():\n",
    "    resp = ['It is Certain', 'It is Decidedly No', 'Without a Doubt', 'Yes', 'Definetly', 'Not a Good Question', 'Are You Kidding Me', 'All Signs Point to No']\n",
    "    rand_resp = random.choice(resp)\n",
    "    return rand_resp\n",
    "\n",
    "def question():\n",
    "    print('Welcome to the Magic 8-Ball Simulator.')\n",
    "    print('Ask me a Yes or No Question.')\n",
    "\n",
    "print(question())\n",
    "user_input = input('Type Your Question Here:')\n",
    "print(response())\n",
    "\n",
    "print('Thank You for Using Magic 8-Ball')\n",
    "\n",
    "   \n",
    "\n",
    "\n",
    "\n",
    "          \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa9d3cf0-4755-4229-9af9-643a95420e69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
