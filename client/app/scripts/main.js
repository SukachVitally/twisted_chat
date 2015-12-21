function ChatView(socket, block) {
    this.socket = socket;
    this.$block = block;

    this.init = function() {
        var self = this;
        this.$message_container = this.$block.find('#chat-content');
        this.$sender = this.$block.find('#sender');

        this.socket.onopen = function() {
            self.renderMessage('--- Connected ---');
        };

        this.socket.onmessage = function(event) {
            self.renderMessage('>>> ' + event.data);
        };

        this.socket.onclose = function(event) {
            if (event.wasClean) {
                self.renderMessage('--- Disconnected ---');
            } else {
                self.renderMessage('--- Server aborted ---');
            }
        };

        this.$sender.on('submit', function(e) {
            e.preventDefault()
            var input = self.$sender.find('input');
            self.sendMessage(input.val());
            input.val('');
        })
    }

    this.renderMessage = function(message) {
        this.$message_container.prepend($('<p>' + message + '</p>'));
    }

    this.sendMessage = function(message) {
        this.socket.send(message)
    }
}

$(function(){
    var socket = new WebSocket("ws://127.0.0.1:8000");
    var chat = new ChatView(socket, $('#chat-block'));
    chat.init();
})


