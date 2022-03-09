FROM TheBlackPantherBot/BLACKPANTHER-USERBOT:alpine

#clonning repo 
RUN git clone https://github.com/TheBlackPantherBot/BlackPantherBot.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","./DANISH_BABA/start.sh"]
