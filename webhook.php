<?php
$bot_name = "nukist_bot";
$bot_api = require('api_key.php');


// Send text back to the sender.
function send_text($post_message, $reply=false) {
  global $decoded;
  global $bot_api;
  global $chat_id;
  $url = 'https://api.telegram.org/bot' . $bot_api . '/sendMessage';
  $post_msg = array('chat_id' => $chat_id, 'text' =>$post_message );
  if ($reply != false) {
    if ($reply === true){
      $post_msg['reply_to_message_id'] = $decoded->{'message'}->{'message_id'};
    }
    else {
      $post_msg['reply_to_message_id'] = $reply;
    }
  }
  $options = array(
    'http' => array(
      'header' => "Content-type: application/x-www-form-urlencoded\r\n",
      'method' => 'POST',
      'content' => http_build_query($post_msg)
    )
  );
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
}

function check_admin($user_id) {
  global $decoded;
  global $bot_api;
  global $chat_id;
  $url = 'https://api.telegram.org/bot' . $bot_api . '/getChatMember';
  $post_msg = array('chat_id' => $chat_id, 'user_id' =>$user_id );
  $options = array(
    'http' => array(
      'header' => "Content-type: application/x-www-form-urlencoded\r\n",
      'method' => 'POST',
      'content' => http_build_query($post_msg)
    )
  );
  $context = stream_context_create($options);
  $result = file_get_contents($url, false, $context);
  $user_json = json_decode($result);
  if ($user_json->{"status"} == "creator" || $user_json->{"status"} == "administrator"){
    return True;
  }
  else {
    return False;
  }
}

// Get JSON from post, store it and decode it.
$var = file_get_contents('php://input');
$decoded = json_decode($var);

// Store the chat ID
$chat_id = $decoded->{"message"}->{"chat"}->{"id"};
$command_list = explode(" ", $decoded->{"message"}->{"text"});

if ($command_list[0] != "/nuke" && $command_list[0] != "/nuke@$bot_name") {
  exit();
}
if ($decoded->{"chat"}->{"type"} != "supergroup" ){
  send_text("The bot only works in supergroups.", True);
  exit();
}

if (!check_admin($decoded->{"chat"}->{"user"}->{"id"})){
  send_text("Only admins can run this");
}

?>
