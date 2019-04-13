
input = ["tom: hi everyone", "jack: hi tom, how are you?", "tom: good, just about to go to lunch.", "betty: did anyone see the email today?"]

def top_talkers(messages, n):
    result = {}
    # M
    for i in messages:
        message = i.split(":")
        name = message[0]
        count_words = len(message[1].split(" "))

        if result.get(name) != "":
            result[name] = count_words
        else:
            result[name] = result[name] + count_words

    # memory: U
    # cpu: U^2
    result = sorted(result, key=lambda x: x[1], reverse=True)

    # N
    return result[0:n]

# O(M) + O(U) + O(N)
print(top_talkers(input, 3))
