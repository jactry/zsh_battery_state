zsh-battery-state
=======================
zsh-battery-state is a plugin to display the state of battery in zsh.


<h3>1.Install oh-my-zsh</h3> 

Follow the guide here:https://github.com/robbyrussell/oh-my-zsh

<h3>2.Clone zsh_battery_state from GitCafé</h3>

git clone git@gitcafe.com:Jactry/zsh_battery_state.git ~/.oh-my-zsh/plugins/zsh_battery_state

<h3>3.Set zsh to support it</h3>

<code>Add this to your ~/.zshrc :

function battery_display {
    BAT_STATE=~/.oh-my-zsh/plugins/zsh_battery_state/battery_state.py
    echo `$BAT_STATE` 2>/dev/null
</p>}
</code>
<code>RPROMPT='$(battery_display)'</code>

<h2>Note:</h2>If does not work in your zsh,please check your .zshrc and make sure it include this:
</p>
<code>ZSH=$HOME/.oh-my-zsh</p>
source $ZSH/oh-my-zsh.sh</code>

 
<h4>Enjoy it!And if you meet some problem when you use it please contact me.My EMail is jactry92@gmail.com Thank you!</h4>

