import discord
import random
import tokens

# Client
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
            
        mes = message.content
        dice_mes = mes.split(' ')
        dice__mes = mes.split('　')

        # ダイスロールのコマンド認識
        """
        command : ダイス, /d
        command mean: ダイスを振る
        """
        dice_rolls = []
        dice_roll_mes = ''
        if dice_mes[0] == 'ダイス':
            dice_roll_mes, dice_rolls = self.dice_roll(dice_mes[1:])
        elif dice__mes[0] == 'ダイス':
            dice_roll_mes, dice_rolls = self.dice_roll(dice__mes[1:])
        elif dice_mes[0] == '/d':
            dice_roll_mes, dice_rolls = self.dice_roll(dice_mes[1:])
        elif dice__mes[0] == '/d':
            dice_roll_mes, dice_rolls = self.dice_roll(dice__mes[1:])

        if not len(dice_rolls) == 0:
            sum_dice = self.sum_dice(dice_rolls)
            dice_roll = ''
            for dice in dice_rolls:
                dice_roll += str(dice) + ' ,'
            await message.channel.send("{}　:  *{}*　**(  {}  )  =  {}**".format(message.author.mention, dice_roll_mes, dice_roll, sum_dice))

        # 隠しダイス
        """
        command : /hd
        command mean: ダイスを振る
        """
        hide_dice_rolls = {}
        if dice_mes[0] == '/hd':
            for user in self.users:
                if user.bot == True or user == message.author:
                    continue
                dice_roll_mes, hide_dice_rolls[user.name] = self.dice_roll(dice_mes[1:])
        elif dice__mes[0] == '/hd':
            for user in self.users:
                if user.bot == True or user == message.author:
                    continue
                dice_roll_mes, hide_dice_rolls[user.name] = self.dice_roll(dice__mes[1:])

        if not len(hide_dice_rolls) == 0:
            dm = await message.author.create_dm()
            dmes = ''
            for hide_dice in hide_dice_rolls:
                sum_dice = self.sum_dice(hide_dice_rolls[hide_dice])
                dice_roll = ''
                for dice in hide_dice_rolls[hide_dice]:
                    dice_roll += str(dice) + ' ,'
                dmes += "{}　:  *{}*  **(  {}  )  =  {}**\n".format(hide_dice, dice_roll_mes, dice_roll, sum_dice)
            await dm.send(dmes)

        # 対抗ロール
        """
        command : /cr 能動 受動
        command mean: 能動と受動によるダイスロール
        """
        counter_dice_rolls = []
        counter_roll_mes = ''
        active = 0
        passive = 0
        if dice_mes[0] == '/cr':
            active = int(dice_mes[1])
            passive = int(dice_mes[2])
            counter_roll_mes, counter_dice_rolls = self.dice_roll(dice_mes[3:])
        elif dice__mes[0] == '/cr':
            active = int(dice__mes[1])
            passive = int(dice__mes[2])
            counter_roll_mes, counter_dice_rolls = self.dice_roll(dice__mes[3:])

        if not len(counter_dice_rolls) == 0:
            sum_dice = self.sum_dice(counter_dice_rolls)
            success = 50 + (active - passive) * 5
            dice_roll = ''
            for dice in counter_dice_rolls:
                if dice <= success:
                    dice_roll += str(dice) + ':成功 ,'
                else:
                    dice_roll += str(dice) + ':失敗 ,'
            await message.channel.send("{}　:  *{}  :  能動-{}  受動-{}  成功値：{}*　**(  {}  )  =  {}**".format(message.author.mention, counter_roll_mes, active, passive, success, dice_roll, sum_dice))

    # ここでダイス用の乱数を実行している
    def dice_roll(self, message):
        mes = ''
        dice_rolls = []
        for mess in message:
            mes += mess
        dice = []
        try:
            if mes == '':
                dice.append(1)
                dice.append(100)
            else:
                dice = [m for m in mes.split('d')]
                if len(dice) == 1:
                    dice = [m for m in mes.split('ｄ')]
                dice = [int(m) for m in dice]
            for i in range(int(dice[0])):
                ran = list(range(1,dice[1]+1))
                random.shuffle(ran)
                random.shuffle(ran)
                random.shuffle(ran)
                dice_rolls.append(random.choice(ran))
        except Exception as e:
            dice.append(0)
            dice.append(0)
            pass
        return '{}d{}'.format(dice[0], dice[1]), dice_rolls

    def sum_dice(self, dice_rolls):
        sum = 0
        for i in dice_rolls:
            sum += i
        return sum

# クライアントの起動
client = MyClient()
# ボットの実行
client.run(tokens.BOT_TOKEN)