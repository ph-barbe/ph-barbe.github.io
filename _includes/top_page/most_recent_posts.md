<table>
{% for post in site.posts limit:3 %}
    <tr>
        <td>
            <a href="{{ post.url }}" class="navigationColor">
                {{ post.title }}
            </a>
        </td>
        <td>
            &nbsp;&nbsp;
            <span class="blogPostDate">
                ({{ post.date | date_to_string }})
            </span>
        </td>
    </tr>
{% endfor %}
</table>