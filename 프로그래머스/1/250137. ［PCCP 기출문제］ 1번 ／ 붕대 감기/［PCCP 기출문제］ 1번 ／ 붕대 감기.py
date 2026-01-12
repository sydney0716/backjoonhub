class Player():
    def __init__(self, max_health, casting_time, heal_per_sec, heal_bonus):
        self.max_health = max_health
        self.current_health = max_health
        self.heal_streak = 0
        self.casting_time = casting_time
        self.heal_bonus = heal_bonus
        self.heal_per_sec = heal_per_sec
        
    def heal(self):
        self.current_health += self.heal_per_sec
        self.heal_streak += 1
        if self.heal_streak == self.casting_time:
            self.current_health += self.heal_bonus
            self.heal_streak = 0
            
        if self.current_health > self.max_health:
            self.current_health = self.max_health
    
    def attack(self, damage):
        self.current_health -= damage
        if self.current_health < 1:
            return 0
        self.heal_streak = 0

def solution(bandage, health, attacks):
    casting_time = bandage[0]
    heal_per_sec = bandage[1]
    heal_bonus = bandage[2]
    attack_counter = 0
    rogue = Player(health, casting_time, heal_per_sec, heal_bonus)
    
    for time in range(attacks[-1][0] + 1):
        incoming_attack_time = attacks[attack_counter][0]
        incoming_attack_damage = attacks[attack_counter][1]
        if time == incoming_attack_time:
            if rogue.attack(incoming_attack_damage) == 0:
                return -1
            attack_counter += 1
        else:
            rogue.heal()
        
    return rogue.current_health