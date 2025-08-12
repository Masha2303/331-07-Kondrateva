using System;
using System.Collections.Generic;

// Класс, представляющий партнёра
public class Partner
{
    public string Name { get; set; } // Имя партнёра
    public string ContactInfo { get; set; } // Контактная информация партнёра
    public List<Dictionary<string, string>> History { get; set; } // История реализации продукции

    public Partner(string name, string contactInfo)
    {
        Name = name;
        ContactInfo = contactInfo;
        History = new List<Dictionary<string, string>>();
    }

    // Добавление записи в историю
    public void AddHistory(string product, string date)
    {
        History.Add(new Dictionary<string, string> { { "product", product }, { "date", date } });
    }
}

// Класс, управляющий списком партнёров
public class PartnerSystem
{
    private List<Partner> partners; // Список партнёров

    public PartnerSystem()
    {
        partners = new List<Partner>();
    }

    // Добавление нового партнёра
    public void AddPartner(string name, string contactInfo)
    {
        Partner partner = new Partner(name, contactInfo);
        partners.Add(partner);
    }

    // Редактирование информации о партнёре
    public void EditPartner(Partner partner, string name = null, string contactInfo = null)
    {
        if (!string.IsNullOrEmpty(name))
        {
            partner.Name = name;
        }
        if (!string.IsNullOrEmpty(contactInfo))
        {
            partner.ContactInfo = contactInfo;
        }
    }

    // Получение списка всех партнёров
    public List<(string Name, string ContactInfo)> ViewPartners()
    {
        List<(string Name, string ContactInfo)> result = new List<(string, string)>();
        foreach (var partner in partners)
        {
            result.Add((partner.Name, partner.ContactInfo));
        }
        return result;
    }

    // Получение истории реализации продукции для конкретного партнёра
    public List<Dictionary<string, string>> ViewHistory(Partner partner)
    {
        return partner.History;
    }
}

// Пример использования
public class Example
{
    public static void Main(string[] args)
    {
        PartnerSystem partnerSystem = new PartnerSystem(); // Создание экземпляра системы партнёров
        partnerSystem.AddPartner("Компания А", "contact@companyA.com"); // Добавление партнёра
        partnerSystem.partners[0].AddHistory("Продукт 1", "2023-01-01"); // Добавление истории реализации

        // Вывод списка партнёров
        var partners = partnerSystem.ViewPartners();
        foreach (var (Name, ContactInfo) in partners)
        {
            Console.WriteLine($"Name: {Name}, ContactInfo: {ContactInfo}");
        }

        // Вывод истории реализации для первого партнёра
        var history = partnerSystem.ViewHistory(partnerSystem.partners[0]);
        foreach (var record in history)
        {
            Console.WriteLine($"Product: {record["product"]}, Date: {record["date"]}");
        }
    }
}
