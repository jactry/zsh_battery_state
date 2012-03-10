zsh_battery_state is a plugin to display the state of battery in zsh.


<h2>1.Install oh-my-zsh</h2> 

Follow the guide here:https://github.com/robbyrussell/oh-my-zsh

<h2>2.Clone zsh_battery_state from GitCafé</h2>

git clone git@gitcafe.com:Jactry/zsh_battery_state.git ~/.oh-my-zsh/plugins/zsh_battery_state

<h2>3.Set zsh to supper it</h2>

<code>Add this to your ~/.zshrc :

function battery_display {
    BAT_STATE=~/.oh-my-zsh/plugins/zsh_battery_state/battery_state.py
    echo `$BAT_STATE` 2>/dev/null
}

RPROMPT='$(battery_display)'</code>

<h3>Enjoy it!And if you meet some problem when you use it please contact me.My EMail is jactry92@gmail.com Thank you!</h3>

